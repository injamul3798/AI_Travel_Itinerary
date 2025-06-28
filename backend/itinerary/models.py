from django.db import models


class Itinerary(models.Model):
    destination = models.CharField(max_length=100)
    date = models.DateField()
    weather_data = models.JSONField(default=dict)
    itinerary_data = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Itineraries"
    
    def __str__(self):
        return f"{self.destination} - {self.date}" 