from django.contrib.auth import authenticate
from rest_framework import status

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny

from django.contrib.auth import authenticate, login
from django.contrib.sessions.models import Session


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            # set user-specific data in the session
            request.session['email'] = email
            request.session.save()
            return Response(f'Logged in. Session Key:{request.session.session_key}', status=status.HTTP_200_OK)
        else:
            return Response('Invalid email or password', status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        request.session.delete()

        return Response({"Logout OK."}, status=status.HTTP_200_OK)

# class LoginView(APIView):
#     permission_classes = [AllowAny]
#
#     def post(self, request):
#         email = request.data.get('email')
#         password = request.data.get('password')
#
#         user = authenticate(request, username=email, password=password)
#         if user:
#             refresh = RefreshToken.for_user(user)
#             return Response({'refresh token': str(refresh), 'access token': str(refresh.access_token)})
#         return Response({'error': 'Invalid email or password'})
#
#
# class RefreshView(APIView):
#     permission_classes = [AllowAny]
#
#     def post(self, request):
#         refresh_token = RefreshToken(request.data.get('refresh_token'))
#         #print(refresh_token)
#
#         if refresh_token:
#             return Response({'new access token': {str(refresh_token.access_token)}})
#         return Response({'error': 'invalid refresh token'})
