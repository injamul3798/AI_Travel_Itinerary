# 🌍 AI Travel Itinerary Builder

A full-stack web application that creates personalized, weather-aware travel itineraries using AI. The app combines real-time weather data with AI-powered recommendations to generate comprehensive travel plans.

## ✨ Features

- **Weather-Aware Planning**: Real-time weather data integration for informed travel decisions
- **AI-Powered Recommendations**: Uses Groq AI to generate personalized itineraries
- **Modern UI**: Beautiful, responsive React frontend with intuitive design
- **RESTful API**: Robust Django backend with comprehensive error handling
- **Fallback Systems**: Multiple weather API providers for reliability
- **Database Storage**: Persistent storage of generated itineraries

## 🏗️ Tech Stack

### Backend

- **Django 5.0+**: Web framework
- **Django REST Framework**: API development
- **SQLite**: Database (can be easily switched to PostgreSQL/MySQL)
- **Python-dotenv**: Environment variable management
- **Requests**: HTTP library for API calls

### Frontend

- **React 18**: UI framework
- **Axios**: HTTP client for API communication
- **CSS3**: Modern styling with gradients and animations

### External APIs

- **RapidAPI Weather**: Primary weather data source
- **OpenWeatherMap**: Fallback weather service
- **Groq AI**: AI-powered itinerary generation

## 📋 Prerequisites

- Python 3.8+
- Node.js 16+
- npm or yarn
- Git

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone <repository-url>
cd travel
```

### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r ../requirements.txt

# Run database migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Start the development server
python manage.py runserver
```

The backend will be available at `http://127.0.0.1:8000`

### 3. Frontend Setup

```bash
# Open a new terminal and navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start the development server
npm start
```

The frontend will be available at `http://localhost:3000`

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the `backend` directory:

```env
GROQ_API_KEY=your_groq_api_key_here
WEATHER_API_KEY=your_rapidapi_weather_key_here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### API Keys Setup

1. **Groq API Key**:

   - Visit [Groq Console](https://console.groq.com/)
   - Sign up and get your API key
   - Add it to your `.env` file

2. **Weather API Key**:
   - Visit [RapidAPI Weather](https://rapidapi.com/weatherapi-com-weatherapi-com-default/api/weatherapi-com/)
   - Subscribe to the API (free tier available)
   - Get your API key and add it to your `.env` file

## 📖 API Endpoints

### Create Itinerary

```
POST /api/itinerary/
Content-Type: application/json

{
    "destination": "Paris",
    "date": "2024-01-15"
}
```

### Get Itinerary

```
GET /api/itinerary/{id}/
```

### List All Itineraries

```
GET /api/itineraries/
```

## 🏃‍♂️ Running the Project

### Development Mode

1. **Start Backend**:

   ```bash
   cd backend
   python manage.py runserver
   ```

2. **Start Frontend** (in a new terminal):

   ```bash
   cd frontend
   npm start
   ```

3. **Access the Application**:
   - Frontend: http://localhost:3000
   - Backend API: http://127.0.0.1:8000
   - Admin Panel: http://127.0.0.1:8000/admin

### Production Deployment

1. **Backend**:

   ```bash
   cd backend
   python manage.py collectstatic
   python manage.py migrate
   # Use a production WSGI server like Gunicorn
   gunicorn travel_itinerary.wsgi:application
   ```

2. **Frontend**:
   ```bash
   cd frontend
   npm run build
   # Serve the build folder with a web server
   ```

## 🗂️ Project Structure

```
travel/
├── backend/
│   ├── itinerary/
│   │   ├── models.py          # Database models
│   │   ├── views.py           # API views
│   │   ├── serializers.py     # Data serialization
│   │   ├── services.py        # Weather and AI services
│   │   └── urls.py            # URL routing
│   ├── travel_itinerary/
│   │   ├── settings.py        # Django settings
│   │   └── urls.py            # Main URL configuration
│   ├── manage.py              # Django management script
│   └── db.sqlite3             # Database file
├── frontend/
│   ├── src/
│   │   ├── App.js             # Main React component
│   │   ├── App.css            # Styles
│   │   └── index.js           # Entry point
│   ├── public/
│   │   └── index.html         # HTML template
│   └── package.json           # Dependencies and scripts
├── requirements.txt           # Python dependencies
└── README.md                 # This file
```

## 🔍 Troubleshooting

### Common Issues

1. **Weather API 401/403 Errors**:

   - Check if your RapidAPI key is valid
   - Verify your subscription includes the weather endpoint
   - The app will automatically fall back to OpenWeatherMap

2. **CORS Errors**:

   - Ensure the backend is running on port 8000
   - Check that `django-cors-headers` is installed
   - Verify CORS settings in `settings.py`

3. **Database Errors**:

   - Run `python manage.py migrate` to apply migrations
   - Check if the database file has proper permissions

4. **Frontend Proxy Issues**:
   - Ensure the backend is running before starting the frontend
   - Check that the proxy setting in `package.json` points to the correct backend URL

### Debug Mode

Enable debug mode by setting `DEBUG=True` in your `.env` file or Django settings.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Weather data provided by RapidAPI and OpenWeatherMap
- AI capabilities powered by Groq
- Built with Django and React

## 📞 Support

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Review the API documentation
3. Open an issue on the repository

---

**Happy Travel Planning! ✈️🌍**
