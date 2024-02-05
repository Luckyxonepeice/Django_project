from rest_framework.views import APIView
from rest_framework.response import Response 
from .models import UserInfo
from .serializers import userInfoSerializer
from django.contrib.auth.hashers import make_password

class Login(APIView):
    
    
    
    def get(self, request, pk=None, format=None):        
        
        if pk is None :
            try:
                user_data = UserInfo.objects.all()
                result = userInfoSerializer(user_data,many=True)
                return Response(result.data)
            except UserInfo.DoesNotExist:
                return Response({"Error":"No Users in Database"},status=404)
            except Exception as error:
                return Response({"Error":f"{error}"},status=400)
            
        else:
            
            try:
                user_data = UserInfo.objects.get(id=pk)
                serialized_data = userInfoSerializer(user_data,many=False)
                result = (serialized_data.data)
                return Response(result)  
            except UserInfo.DoesNotExist:
                return Response({"Error":"User Not Found"}, status=404) 
            except Exception as error:
                return Response({"Error":f"{error}"},status=400)
        
             
    def post(self, request,format=None):
        
        data = request.data
        
        obj = userInfoSerializer(data=data)
        
        
        
        if obj.is_valid(raise_exception=True):
            
            try:
                obj.save()
                
            except Exception as error:
                
                return Response(obj.error_messages)
            
        
        return Response({"message:User Created"})