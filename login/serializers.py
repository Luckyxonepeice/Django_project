from rest_framework import serializers
from .models import UserInfo , EmailVerify
from django.contrib.auth.hashers import make_password

        
class userInfoSerializer(serializers.ModelSerializer):
    
    
        
    class Meta:
        model = UserInfo
        fields = ['first_name','last_name','email','is_verified','password']
        
        
    # def prev_otp(self , data):
        
    #     '''
    #         Custom Validator to Check if Previous any Token Generated for this User
    #     '''
        
    #     try:
    #         instance = UserInfo.objects.get(email=data)
    #         if instance.verify.exists():
    #             raise serializers.ValidationError('Already Contained the OTP for Verification')
    #     except:
    #         pass

    
    # def validate(self, data):
    #     '''
    #         Custom Validators 
    #     '''
    #     self.prev_otp(data['email'])
        
    #     return data
        
        
    def create(self ,validated_data):
        
        '''
            Storing Hashed Password of User during create 
        '''
        
        password = validated_data['password']
        validated_data['password'] = make_password(password)
        
        return UserInfo.objects.create(**validated_data)
    
    


class EmailVerifySerializer(serializers.ModelSerializer):
    
    user_verify = userInfoSerializer()
    
    class Meta:
        model = EmailVerify 
        fields = ["time_limit","email_token","user_verify"]
        
    
    