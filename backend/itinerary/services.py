import requests
import groq
from django.conf import settings
from datetime import datetime
import json


class WeatherService:
    """Service for fetching weather data from Weather APIs with fallback"""
    
    def __init__(self):
        self.api_key = settings.WEATHER_API_KEY
        self.base_url = "https://weather-api167.p.rapidapi.com"
        self.headers = {
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": "weather-api167.p.rapidapi.com",
            "Accept": "application/json"
        }
    
    def get_weather(self, city, date):
        """Get weather forecast for a specific city and date"""
        try:
            # Try RapidAPI first
            return self._get_weather_rapidapi(city, date)
        except Exception as e:
            # Fallback to OpenWeatherMap
            try:
                return self._get_weather_openweathermap(city, date)
            except Exception as fallback_error:
                raise Exception(f"Weather API error: {str(e)}. Fallback also failed: {str(fallback_error)}")
    
    def _get_weather_rapidapi(self, city, date):
        """Get weather from RapidAPI"""
        try:
            # Get weather forecast using the exact working endpoint
            weather_url = f"{self.base_url}/api/weather/forecast"
            weather_params = {
                'place': f"{city},GB",  # Using GB as default country like in the curl command
                'cnt': '3',  # Get 3 forecasts like in the curl command
                'units': 'standard',
                'type': 'three_hour',
                'mode': 'json',
                'lang': 'en'
            }
            
            weather_response = requests.get(weather_url, headers=self.headers, params=weather_params)
            weather_response.raise_for_status()
            
            weather_data = weather_response.json()
            
            # Parse the response based on the API structure
            if 'list' not in weather_data:
                raise ValueError(f"Weather data not available for '{city}'")
            
            # Get the first available forecast (most current)
            if weather_data['list']:
                day = weather_data['list'][0]
                main_data = day.get('main', {})
                weather_info = day.get('weather', [{}])[0]
                wind_data = day.get('wind', {})
                
                return {
                    'temperature': main_data.get('temp', 0),
                    'description': weather_info.get('description', 'Unknown'),
                    'main': weather_info.get('main', 'Unknown'),
                    'humidity': main_data.get('humidity', 0),
                    'wind_speed': wind_data.get('speed', 0)
                }
            
            raise ValueError(f"No weather data found for '{city}'")
            
        except requests.RequestException as e:
            raise Exception(f"RapidAPI error: {str(e)}")
    
    def _get_weather_openweathermap(self, city, date):
        """Get weather from OpenWeatherMap as fallback"""
        try:
            # OpenWeatherMap API (free tier)
            api_key = "demo"  # You can replace this with a real OpenWeatherMap API key
            weather_url = "http://api.openweathermap.org/data/2.5/weather"
            weather_params = {
                'q': city,
                'appid': api_key,
                'units': 'metric'
            }
            
            weather_response = requests.get(weather_url, params=weather_params)
            weather_response.raise_for_status()
            
            weather_data = weather_response.json()
            
            # Get the weather data
            main_data = weather_data.get('main', {})
            weather_info = weather_data.get('weather', [{}])[0]
            wind_data = weather_data.get('wind', {})
            
            return {
                'temperature': main_data.get('temp', 0),
                'description': weather_info.get('description', 'Unknown'),
                'main': weather_info.get('main', 'Unknown'),
                'humidity': main_data.get('humidity', 0),
                'wind_speed': wind_data.get('speed', 0)
            }
            
        except requests.RequestException as e:
            raise Exception(f"OpenWeatherMap error: {str(e)}")


class GroqService:
    """Service for generating itineraries using Groq API"""
    
    def __init__(self):
        self.client = groq.Groq(api_key=settings.GROQ_API_KEY)
    
    def generate_itinerary(self, destination, date, weather_data):
        """Generate a weather-aware travel itinerary using Groq API"""
        try:
            weather_summary = f"Temperature: {weather_data['temperature']}°C, Weather: {weather_data['description']}, Humidity: {weather_data['humidity']}%, Wind Speed: {weather_data['wind_speed']} m/s"
            
            prompt = f"""
            Create a detailed day-wise travel itinerary for {destination} on {date}.
            
            Weather Information: {weather_summary}
            
            Please provide a comprehensive itinerary that includes:
            1. Morning activities (breakfast, sightseeing, etc.)
            2. Afternoon activities (lunch, exploration, etc.)
            3. Evening activities (dinner, entertainment, etc.)
            4. Weather-appropriate recommendations (indoor activities if rainy, outdoor activities if sunny, etc.)
            5. Local food recommendations
            6. Transportation suggestions
            7. Estimated costs for activities and meals
            
            Format the response as a structured JSON with the following structure:
            {{
                "morning": {{
                    "activities": ["activity1", "activity2"],
                    "food": "recommendation",
                    "transportation": "suggestion",
                    "estimated_cost": "cost range"
                }},
                "afternoon": {{
                    "activities": ["activity1", "activity2"],
                    "food": "recommendation",
                    "transportation": "suggestion",
                    "estimated_cost": "cost range"
                }},
                "evening": {{
                    "activities": ["activity1", "activity2"],
                    "food": "recommendation",
                    "transportation": "suggestion",
                    "estimated_cost": "cost range"
                }},
                "weather_notes": "specific weather-related recommendations",
                "total_estimated_cost": "total cost range for the day"
            }}
            
            Make sure the itinerary is practical, enjoyable, and takes into account the weather conditions.
            """
            
            response = self.client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,
                max_tokens=2000
            )
            
            # Extract the JSON response
            content = response.choices[0].message.content
            
            # Try to parse JSON from the response
            try:
                # Find JSON content in the response
                start_idx = content.find('{')
                end_idx = content.rfind('}') + 1
                if start_idx != -1 and end_idx != 0:
                    json_str = content[start_idx:end_idx]
                    itinerary_data = json.loads(json_str)
                else:
                    # If no JSON found, create a structured response
                    itinerary_data = {
                        "morning": {
                            "activities": ["Explore local attractions"],
                            "food": "Local breakfast recommendation",
                            "transportation": "Walking or public transport",
                            "estimated_cost": "$10-20"
                        },
                        "afternoon": {
                            "activities": ["Visit museums or landmarks"],
                            "food": "Local lunch recommendation",
                            "transportation": "Walking or public transport",
                            "estimated_cost": "$15-30"
                        },
                        "evening": {
                            "activities": ["Dinner and entertainment"],
                            "food": "Local dinner recommendation",
                            "transportation": "Walking or public transport",
                            "estimated_cost": "$20-40"
                        },
                        "weather_notes": f"Weather-aware recommendations based on {weather_data['description']}",
                        "total_estimated_cost": "$45-90"
                    }
                
                return itinerary_data
                
            except json.JSONDecodeError:
                # If JSON parsing fails, return a structured fallback
                return {
                    "morning": {
                        "activities": ["Explore local attractions"],
                        "food": "Local breakfast recommendation",
                        "transportation": "Walking or public transport",
                        "estimated_cost": "$10-20"
                    },
                    "afternoon": {
                        "activities": ["Visit museums or landmarks"],
                        "food": "Local lunch recommendation",
                        "transportation": "Walking or public transport",
                        "estimated_cost": "$15-30"
                    },
                    "evening": {
                        "activities": ["Dinner and entertainment"],
                        "food": "Local dinner recommendation",
                        "transportation": "Walking or public transport",
                        "estimated_cost": "$20-40"
                    },
                    "weather_notes": f"Weather-aware recommendations based on {weather_data['description']}",
                    "total_estimated_cost": "$45-90",
                    "ai_response": content
                }
                
        except Exception as e:
            raise Exception(f"Error generating itinerary: {str(e)}") 