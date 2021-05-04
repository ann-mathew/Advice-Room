from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from users.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

"""
    API Response Table:

    400: Invalid POST
    200: Success
    401: Authentication error

"""

@api_view(['POST'])  
def register_user(request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.data
            user['password'] = make_password(user['password'])
            user = User.objects.create(username=user['username'], email=user['email'], password=user['password'])
            if user:
                json = serializer.data
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key, 'user_id': user.user_id}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_user(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key, 'user_id': user.user_id} , status=status.HTTP_200_OK)

                   
