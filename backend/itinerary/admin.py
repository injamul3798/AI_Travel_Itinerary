from django.contrib import admin
from .models import Itinerary


@admin.register(Itinerary)
class ItineraryAdmin(admin.ModelAdmin):
    list_display = ('destination', 'date', 'created_at')
    list_filter = ('destination', 'date', 'created_at')
    search_fields = ('destination',)
    readonly_fields = ('created_at',)
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('destination', 'date')
        }),
        ('Data', {
            'fields': ('weather_data', 'itinerary_data')
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    ) 