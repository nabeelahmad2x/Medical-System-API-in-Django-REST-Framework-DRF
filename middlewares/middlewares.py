import jwt
# from importlib import import_module
# from django.conf import settings

from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

# from rest_framework import status

from users.models import CustomUser


class TokenModelTrackerMiddleware(MiddlewareMixin):
    def __call__(self, request):
        auth_header = request.headers.get('Authorization')

        if auth_header:
            token = auth_header[len('bearer '):].strip()

            # this one is for extracting if JWT token is sent in request..
            payload = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=['HS256'])

            # this one is for extracting csrf key sent in request..
            # SessionStore = import_module(settings.SESSION_ENGINE).SessionStore
            # payload = SessionStore().decode(token)

            user = CustomUser.objects.get(id=payload['user_id'])

            if user:
                request.user_type = user.user_type
            else:
                request.user_type = "404: User Not Found :D"
        else:
            request.user_type = "No Auth Info in header."
        print(request.user_type)
        response = self.get_response(request)
        return response
