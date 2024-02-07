from rest_framework.views import APIView
from rest_framework.response import Response 
from .models import UserInfo, EmailVerify as EmailCheck
from .serializers import userInfoSerializer, EmailVerifySerializer
from .utils import otpGenerator
from datetime import datetime
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
                
                user_object=(obj.save())
                
                otp = otpGenerator(4)
                
                dt = datetime.now()
                
                dt_str = dt.isoformat() 
                try:
                    
                    Email_token = EmailCheck.objects.create(user_verify=user_object, email_token = otp,
                                                            time_limit=dt_str)

                except Exception as error:
                    
                    return Response({"Error":str(error)}, status=404)
                         
                
                
            except Exception as error:
                
                return Response({"Error":str(error)})
            
        return Response({"message":"User Created"})
    
    

class EmailVerify(APIView):
    
    def post(self, request , pk , format=None):
        
        otp = request.data
        
        user_obj = None
        try:
            
            user_obj = UserInfo.objects.get(id=pk)
            
        except Exception as error:
            
            return Response({"Error":f"{error}"})
        
        try:
            
            email_obj = user_obj.verify.get(email_token=otp)
        except Exception as error:
            return Response({"Error":str(error)})
                        
        return Response({"Message!"})
            
            
        
        
        