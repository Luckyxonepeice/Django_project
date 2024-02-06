from django.contrib import admin
from .models import UserInfo, EmailVerify
# Register your models here.
admin.site.register(UserInfo)
admin.site.register(EmailVerify)