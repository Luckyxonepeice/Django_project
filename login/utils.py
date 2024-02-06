from random import randint

def otpGenerator(size):
    '''
        Creating the OTP the length Provided to it.
        
    '''
    
    if(size<=3): raise Exception("Sorry need to Be Size greater than 4")
    
    end =0
    for i in range(size):
        end= end*10+9
        
    value = randint(pow(10,size-1),end)
    
    return value

