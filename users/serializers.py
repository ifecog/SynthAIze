from typing import Dict, Any

from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, RefreshToken


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = get_user_model()
        fields = ['uuid', 'name', 'email', 'role', 'isAdmin']
        
                
    def get_name(self, obj):
        name = f'{obj.first_name} {obj.last_name}' if obj.first_name or obj.last_name else obj.email
        return name
        
        
    def get_isAdmin(self, obj):
        return obj.is_staff
        
        
class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = get_user_model()
        fields = ['uuid', 'first_name', 'last_name', 'email', 'role', 'bio', 'password', 'isAdmin', 'token']
        
        
    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        
        return str(token.access_token)
    
    
class SigninSerializer(TokenObtainPairSerializer):
    token_class = RefreshToken
    
    
    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        email = attrs.get('email', None)
        password = attrs.get('password', None)
        
        try:
            user = get_user_model().objects.get(email=email)
        except get_user_model().DoesNotExist:
            raise AuthenticationFailed(detail=_('No account found with this email.'))
        
        user = authenticate(email=email, password=password)
        if user is None:
            raise AuthenticationFailed(detail=_('Incorrect password!'))
        
        
        data = super().validate(attrs)
        
        # serializer = UserSerializerWithToken(self.user).data

        # for key, value in serializer.items():
        #     data[key] = value
        
        serializer = UserSerializerWithToken(user)
        data['name'] = f'{serializer.data.get('first_name')} {serializer.data.get('last_name')}'
        data['email'] = serializer.data.get('email')
        data['role'] = serializer.data.get('role')
        data['isAdmin'] = serializer.data.get('isAdmin')
        data['token'] = serializer.data.get('token')
        
        return data
    
    
class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(required=True, write_only=True)
    confirm_password = serializers.CharField(required=True, write_only=True)

    class Meta:
        fields = ['old_password', 'new_password', 'confirm_password']