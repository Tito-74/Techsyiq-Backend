from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from rest_framework import status
from .serializers import CourseSerializer
from .models import Course
# Create your views here.

# add team member
@api_view(['POST'])
@csrf_exempt
def add_course_details(request):
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# get all members
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_course(request):
    course = Course.objects.all()
    serializer = CourseSerializer(course, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# update member details
@api_view(['PUT'])
@csrf_exempt
def update_course_details(request, pk):
    # pk = kwargs.get('pk')
    print(pk)
    try:
        course = Course.objects.filter(id=pk).first()
        print(course)
    except course.DoesNotExist:
        return Response({"message":"Course does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = CourseSerializer(instance=course, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"Course updated successfully"}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_course_details(request, pk):
    # pk = kwargs.get('pk')
    try:
        course = Course.objects.filter(id=pk).first()
    
    except course.DoesNotExist:
        return Response({"message":"Course does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    course.delete()

    return Response({"message":"Course deleted successfully"}, status=status.HTTP_200_OK)
