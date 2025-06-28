from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone
from .serializers import ItineraryRequestSerializer, ItineraryResponseSerializer
from .services import WeatherService, GroqService
from .models import Itinerary


@api_view(['POST'])
def create_itinerary(request):
    """
    Create a weather-aware travel itinerary
    """
    try:
        # Validate input data
        serializer = ItineraryRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {'error': 'Invalid input data', 'details': serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        destination = serializer.validated_data['destination']
        date = serializer.validated_data['date']
        
        # Check if date is in the future
        if date < timezone.now().date():
            return Response(
                {'error': 'Date must be in the future'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Get weather data
        weather_service = WeatherService()
        try:
            weather_data = weather_service.get_weather(destination, date.strftime('%Y-%m-%d'))
            if not weather_data:
                return Response(
                    {'error': f'Unable to fetch weather data for {destination}'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return Response(
                {'error': f'Weather service error: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
        # Generate itinerary using Groq API
        groq_service = GroqService()
        try:
            itinerary_data = groq_service.generate_itinerary(destination, date.strftime('%Y-%m-%d'), weather_data)
        except Exception as e:
            return Response(
                {'error': f'Itinerary generation error: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
        # Save to database
        itinerary = Itinerary.objects.create(
            destination=destination,
            date=date,
            weather_data=weather_data,
            itinerary_data=itinerary_data
        )
        
        # Return response
        response_serializer = ItineraryResponseSerializer(itinerary)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        
    except Exception as e:
        return Response(
            {'error': f'Unexpected error: {str(e)}'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
def get_itinerary(request, itinerary_id):
    """
    Get a specific itinerary by ID
    """
    try:
        itinerary = Itinerary.objects.get(id=itinerary_id)
        serializer = ItineraryResponseSerializer(itinerary)
        return Response(serializer.data)
    except Itinerary.DoesNotExist:
        return Response(
            {'error': 'Itinerary not found'},
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response(
            {'error': f'Unexpected error: {str(e)}'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
def list_itineraries(request):
    """
    List all itineraries
    """
    try:
        itineraries = Itinerary.objects.all().order_by('-created_at')
        serializer = ItineraryResponseSerializer(itineraries, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response(
            {'error': f'Unexpected error: {str(e)}'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        ) 