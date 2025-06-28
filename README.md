# 🌍 AI Travel Itinerary Builder


https://github.com/user-attachments/assets/c009535d-8432-4bff-8c11-3bb1987ab89e


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
git [clone https://github.com/injamul3798/AI_Travel_Itinerary
cd AI_Travel_Itinerary
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

## 👨‍💻 Developed By

### Injamul Haque  
💼 Machine Learning Engineer at [DevtechGuru Limited]


