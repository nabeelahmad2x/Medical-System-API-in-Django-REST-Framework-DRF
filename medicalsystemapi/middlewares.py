import jwt
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

from rest_framework import status


from users.models import CustomUser

class TokenModelTrackerMiddleware(MiddlewareMixin):
    def __call__(self, request):
        #print('middleware 1--------------------------------------------')
        auth_header = request.headers.get('Authorization')
        
        if auth_header:
            #print('middleware 2--------------------------------------------')
            token = auth_header[len('bearer '):].strip()

            payload = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=['HS256'])
        
            user = CustomUser.objects.get(id=payload['user_id'])
            

            if user:
                #print('middleware 3--------------------------------------------')
                if user.is_staff:
                    #print('middleware 4--------------------------------------------')
                    request.user_type = "Doctor"
                else:
                    request.user_type = "Patient"
            else:
                request.user_type = "404: User Not Found :D"
        else:
            request.user_type = "No Auth Info in header."
        print(request.user_type)
        response = self.get_response(request)
        return response