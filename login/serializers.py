from rest_framework import serializers
from .models import UserInfo
from django.contrib.auth.hashers import make_password
class userInfoSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = UserInfo
        fields = ['first_name','last_name','email','is_verified','password']
    
    def create(self ,validated_data):
        
        '''
            Storing Hashed Password of User during create 
        '''
        
        password = validated_data['password']
        validated_data['password'] = make_password(password)
        
        return UserInfo.objects.create(**validated_data)
        