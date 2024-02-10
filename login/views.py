from rest_framework.views import APIView
from rest_framework.response import Response 
from .models import UserInfo, EmailVerify as EmailCheck
from .serializers import userInfoSerializer, EmailVerifySerializer
from .utils import otpGenerator
from datetime import datetime,timedelta
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
        
        data = request.data
        
        otp = data['token']
        

        try:
            
            user_obj = UserInfo.objects.get(id=pk)
            
            try:
                email_obj = user_obj.verify.get(email_token=otp)
                
                #Validating Time Limit Of One Day
                user_date = email_obj.time_limit.replace(tzinfo=None)
                
                Diff = datetime.now().replace(tzinfo=None)-user_date
                
                one_day = timedelta(days=1)
                print(one_day)
                if Diff>one_day:
                    raise Exception("OTP validity Vanished!!")
                
                email_obj.delete()
                
                user_obj.is_verified=True
                
                user_obj.save()
                
            except EmailCheck.DoesNotExist:
                
                return Response({"Error":"Not Valid Token!"}, status=422)
            
            except Exception as error:
                
                return Response({"Error":str(error)})
            
                                            
        except Exception as error:
            
            return Response({"Error":f"{error}"})
        
          
        return Response({"Message":"SuccessFully Logged IN!"})
            
            
        
        
        