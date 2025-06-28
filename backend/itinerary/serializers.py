from rest_framework import serializers
from .models import Itinerary


class ItineraryRequestSerializer(serializers.Serializer):
    destination = serializers.CharField(max_length=100)
    date = serializers.DateField()


class ItineraryResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Itinerary
        fields = ['id', 'destination', 'date', 'weather_data', 'itinerary_data', 'created_at'] 