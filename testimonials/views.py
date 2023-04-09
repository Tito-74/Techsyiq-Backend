from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from rest_framework import status
from .serializers import TestimonialSerializer
from .models import Testimonial
# Create your views here.

# add testimonial member
@api_view(['POST'])
@csrf_exempt
def add_testimonial_details(request):
    serializer = TestimonialSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# get all members
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_testimonial(request):
    testimonial = Testimonial.objects.all()
    serializer = TestimonialSerializer(testimonial, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# update member details
# @api_view(['PUT'])
# @csrf_exempt
# def update_testimonia_details(self, request, *args, **kwargs):
#     pk = kwargs.get('pk')
#     try:
#         testimonial = Testimonial.Objects.filter(id=pk).first()
    
#     except testimonial.DoesNotExist:
#         return Response({"message":"Testimonial does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
#     serializer = TestimonialSerializer(instance=testimonial, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({"message":"Testimonial updated successfully"}, status=status.HTTP_200_OK)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_testimonial_details(self, request, *args, **kwargs):
    pk = kwargs.get('pk')
    try:
        testimonial = Testimonial.Objects.filter(id=pk).first()
    
    except testimonial.DoesNotExist:
        return Response({"message":"Testimonial does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    testimonial.delete()

    return Response({"message":"Testimonial deleted successfully"}, status=status.HTTP_200_OK)
