from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import BlogSerializer, CategorySerializer
from .models import Category, Blog
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect, csrf_exempt 

# Create your views here.
# create category view
@api_view(['POST'])
# @permission_classes([AllowAny])
@csrf_exempt
def create_category(request):
    serializer = CategorySerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# getting all category in db
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_category(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)