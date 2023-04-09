from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from rest_framework import status
from .serializers import TeamSerializer
from .models import Team
# Create your views here.

# add team member
@api_view(['POST'])
@csrf_exempt
def add_team_member(request):
    serializer = TeamSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# get all members
@api_view(['GET'])
@permission_classes([AllowAny])
def get_members(request):
    members = Team.objects.all()
    serializer = TeamSerializer(members, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

