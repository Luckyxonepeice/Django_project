from django.db import models
from datetime import datetime 
class UserInfo(models.Model):
    
    first_name = models.CharField(blank=False,max_length=15)
    last_name = models.CharField(blank=False, max_length=15)
    email = models.EmailField(null=False , unique=True,blank=False, default='')
    password = models.TextField(null=False,blank=False)
    
    is_verified = models.BooleanField(default=False)
    

class EmailVerify(models.Model):
    
    user_verify = models.ForeignKey(UserInfo,on_delete=models.CASCADE, null=True, related_name="verify")
    email_token = models.IntegerField(blank=False)
    time_limit = models.DateTimeField(default=datetime.now())


