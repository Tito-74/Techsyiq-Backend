from rest_framework import serializers
from .models import FiguresAnalysis, Subscription

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"



class FigureAnalysisSerializer(serializers.ModelSerializer):
     class Meta:
        model = Subscription
        fields = "__all__"