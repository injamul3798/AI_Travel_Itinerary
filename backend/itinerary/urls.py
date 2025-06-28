from django.urls import path
from . import views

urlpatterns = [
    path('itinerary/', views.create_itinerary, name='create_itinerary'),
    path('itinerary/<int:itinerary_id>/', views.get_itinerary, name='get_itinerary'),
    path('itineraries/', views.list_itineraries, name='list_itineraries'),
] 