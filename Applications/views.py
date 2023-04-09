from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from rest_framework import status
from .serializers import ApplicationSerializer
from .models import Application

# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_exempt
def create_application(request, *args, **kwargs):
    serializer = ApplicationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# view application
@api_view(['GET'])
def get_all_application_details(request):
    application = Application.objects.all()
    serializer = ApplicationSerializer(application, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

