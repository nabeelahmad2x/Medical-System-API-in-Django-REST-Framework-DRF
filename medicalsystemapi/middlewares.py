import jwt
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

from rest_framework import status
from rest_framework.response import Response

from users.models import CustomUser

class TokenModelTrackerMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response
    print('middleware 1--------------------------------------------')
    def __call__(self, get_response):
        self.get_response = get_response
    def process_response(self, request):
        auth_header = request.headers.get('Authorization')
        print('middleware 2--------------------------------------------')
        token = auth_header[len('bearer '):]

        payload = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=['HS256'])
        print('middleware 3--------------------------------------------')
        user = CustomUser.objects.get(id=payload['user_id'])

        if user:
            print('middleware 4--------------------------------------------')
            if user.is_staff == True:
                return Response({'Request made by Doctor'})
            return Response({'Request made by Patient'})
        return Response({'Invalid or Expired Token.'}, status=status.HTTP_400_BAD_REQUEST)