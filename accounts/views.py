from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework import exceptions
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect, csrf_exempt
from accounts.utils import generate_access_token, generate_refresh_token
import jwt
from django.conf import settings

# Create your views here.

# view user details
@api_view(['GET'])
def profile(request):
    user = request.user
    serialized_user = UserSerializer(user).data
    return Response({'user':serialized_user})


# login
@api_view(['POST'])
@permission_classes([AllowAny])
@ensure_csrf_cookie
def login_view(request):
    User = get_user_model()
    username = request.data.get('username')
    password =request.data.get('password')
   
    response = Response()
    if (username is None) or (password is None):
        raise exceptions.AuthenticationFailed('username and password is required')
    user = User.objects.filter(username=username).first()
    if user is None:
        raise exceptions.AuthenticationFailed('User not found')
    if not user.check_password(password):
        raise exceptions.AuthenticationFailed('Wrong password')
    
    serialized_user = UserSerializer(user).data

    access_token = generate_access_token(user)
    refresh_token = generate_refresh_token(user)

    response.set_cookie(key='refreshtoken', value=refresh_token, httponly=True)
    response.data = {
        'access_token': access_token,
        'user':serialized_user,
    }
    return response

# refresh token
@api_view(['POST'])
@permission_classes([AllowAny])
# @csrf_protect
@csrf_exempt
def refresh_token_view(request):
    User = get_user_model()
    refresh_token = request.COOKIES.get('refreshtoken')
    print("refresh token:", refresh_token)
    if refresh_token is None:
        raise exceptions.AuthenticationFailed('Authentication credentials were not provided')
    
    try:
        payload = jwt.decode(refresh_token, settings.REFRESH_TOKEN_SECRET_KEY, algorithms=['HS256'])

    except jwt.ExpiredSignatureError:
        raise exceptions.AuthenticationFailed('Refresh token has expired, please login')
    
    user = User.objects.filter(id=payload.get('user_id')).first()
    print("user:", user)
    if user is None:
        raise exceptions.AuthenticationFailed('user does not exist')
    if not user.is_active:
        raise exceptions.AuthenticationFailed('user is inactive')
    
    access_token = generate_access_token(user)

    return Response({'access_token': access_token})
    



