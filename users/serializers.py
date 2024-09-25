from typing import Dict, Any

from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, RefreshToken


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = get_user_model()
        fields = ['uuid', 'name', 'email', 'role', 'isAdmin']
        
                
    def get_name(self, obj):
        name = ''
         
        try:
            name = f'{obj.first_name} {obj.last_name}'
            # name = obj.first_name + ' ' + obj.last_name
            if not name:
                return obj.email
        except:
            pass
            
        return name
        
        
    def get_isAdmin(self, obj):
        return obj.is_staff
        
        
class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = get_user_model()
        fields = ['uuid', 'name', 'email', 'role', 'isAdmin', 'token']
        
        
    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        
        return str(token.access_token)
    
    
class SigninSerializer(TokenObtainPairSerializer):
    token_class = RefreshToken
    
    
    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        data = super().validate(attrs)
        
        serializer = UserSerializerWithToken(self.user).data

        for key, value in serializer.items():
            data[key] = value
        
        return data