from django.contrib.auth.hashers import make_password

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User
from users.serializers import (
    UserSerializer,
    UserSerializerWithToken,
    SigninSerializer
)


class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializerWithToken
    permission_classes = [AllowAny]
    
    
    def create(self, request, *args, **kwargs):
        data = request.data
        
        if User.objects.filter(email=data['email']).exists():
            return Response({'detail': 'Email already in use!'}, status=status.HTTP_400_BAD_REQUEST)
        
        role = data.get('role', 'observer')
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