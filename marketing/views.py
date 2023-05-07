from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny 


from .models import FiguresAnalysis, Subscription
from .serializers import FigureAnalysisSerializer, SubscriptionSerializer
# Create your views here.

# FiguresAnalysis
@api_view(["POST"])
@csrf_exempt
def create_figure_analysis(request):
    # figure = FiguresAnalysis.objects.all()
    serializer = FigureAnalysisSerializer(data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
@permission_classes(["AllowAny"])
def fetch_figure_analysis(request):
    figure = FiguresAnalysis.objects.all()

    serializer = FigureAnalysisSerializer(figure, many=True)
    return Response(serializer.data, status = status.HTTP_200_OK)


@api_view(["PUT"])
@csrf_exempt
def update_figures_details(request, pk):
   
   try:
      figure = FiguresAnalysis.objects.get(id=pk)

   except figure.DoesNotExist:
      return Response({"message":"Details does not exist"})
   
   serializer = FigureAnalysisSerializer(instance = figure, data = request.data)
   if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status = status.HTTP_200_OK)
   return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)
   


# Subscription
