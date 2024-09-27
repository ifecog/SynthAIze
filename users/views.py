from django.contrib.auth.hashers import check_password, make_password

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User
from users.permissions import isAdminOrOwner
from users.serializers import (
    UserSerializer,
    UserSerializerWithToken,
    SigninSerializer,
    PasswordChangeSerializer,
)


class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializerWithToken
    permission_classes = [AllowAny]
    
    
    def create(self, request, *args, **kwargs):
        data = request.data
        
        if User.objects.filter(email=data['email']).exists():
            return Response({'detail': 'Email already in use!'}, status=status.HTTP_400_BAD_REQUEST)
        
        role = data.get('role', 'Observer')
        if role == 'Synthesist' and not data.get('bio'):
            return Response({'detail': 'Bio is required for Synthesists'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.create(
                first_name=data.get('first_name', ''),
                last_name=data.get('last_name', ''),
                email=data['email'],
                bio=data.get('bio', ''),
                role=role,
                password=make_password(data['password'])
            )
            
            serializer = self.get_serializer(user)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)



class SigninView(TokenObtainPairView):
    serializer_class = SigninSerializer
    
    
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    

class SynthesistListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    
    def get_queryset(self):
        return User.objects.filter(role='Synthesist')
    
    
class ObserverListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    
    def get_queryset(self):
        return User.objects.filter(role='Observer')
    
    
class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser, isAdminOrOwner]
    lookup_field = 'uuid'
    
    
class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, isAdminOrOwner]
    lookup_field = 'uuid'
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        user = self.get_object()
        data = request.data
        
        user.first_name = data.get('first_name', user.first_name)
        user.last_name = data.get('last_name', user.last_name)
        user.bio = data.get('bio', user.bio)
        user.role = data.get('role', user.role)
        
        user.save()
        
        serializer = self.get_serializer(user, partial=partial)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class PasswordUpdateView(generics.GenericAPIView):
    serializer_class = PasswordChangeSerializer
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        
        if not check_password(data['old_password'], user.password):
            return Response({'detail': 'Old password is incorrect!'}, status=status.HTTP_400_BAD_REQUEST)
        
        if data['new_password'] != data['confirm_password']:
            return Response({'detail': 'New password and confirm password do not match!'}, status=status.HTTP_400_BAD_REQUEST)
        
        user.password = make_password(data['new_password'])
        user.save()
        
        return Response({'detail': 'Password updated successfully!'}, status=status.HTTP_200_OK)
    
    
class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'uuid'
    
    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        self.perform_destroy(user)
        
        return Response({'detail': 'User successfully deleted!'},status=status.HTTP_200_OK)