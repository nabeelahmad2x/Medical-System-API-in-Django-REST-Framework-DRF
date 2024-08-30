from django.contrib.auth import authenticate

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny


class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        #print('point 1-------------------------------------')
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, username=email, password=password)
        #print('point 2-------------------------------------')

        if user:
            #print('point 3-------------------------------------')
            refresh = RefreshToken.for_user(user)
            #print('point 4-------------------------------------')
            return Response({'refresh token': str(refresh), 'access token': str(refresh.access_token)})        
        return Response({'error': 'Invalid email or password'})


class RefreshView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        refresh_token = RefreshToken(request.data.get('refresh_token'))
        #print(refresh_token)

        if refresh_token:
            return Response({'new access token': {str(refresh_token.access_token)}})
        return Response({'error': 'invalid refresh token'})
    
    