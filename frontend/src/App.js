import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
    const [formData, setFormData] = useState({
        destination: '',
        date: ''
    });
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');
    const [itinerary, setItinerary] = useState(null);

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setFormData(prev => ({
            ...prev,
            [name]: value
        }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError('');
        setItinerary(null);

        try {
            const response = await axios.post('/api/itinerary/', formData);
            setItinerary(response.data);
        } catch (err) {
            if (err.response?.data?.error) {
                setError(err.response.data.error);
            } else if (err.response?.data?.details) {
                setError(Object.values(err.response.data.details).flat().join(', '));
            } else {
                setError('An unexpected error occurred. Please try again.');
            }
        } finally {
            setLoading(false);
        }
    };

    const formatDate = (dateString) => {
        const date = new Date(dateString);
        return date.toLocaleDateString('en-US', {
            weekday: 'long',
            year: 'numeric',
            month: 'long',
            day: 'numeric'
        });
    };

    const renderTimeSection = (timeData, title) => {
        if (!timeData) return null;

        return (
            <div className="time-section">
                <h3>{title}</h3>
                {timeData.activities && timeData.activities.length > 0 && (
                    <ul className="activity-list">
                        {timeData.activities.map((activity, index) => (
                            <li key={index}>{activity}</li>
                        ))}
                    </ul>
                )}
                <div className="detail-item">
                    <span className="detail-label">Food:</span>
                    <span className="detail-value">{timeData.food || 'Not specified'}</span>
                </div>
                <div className="detail-item">
                    <span className="detail-label">Transportation:</span>
                    <span className="detail-value">{timeData.transportation || 'Not specified'}</span>
                </div>
                <div className="detail-item">
                    <span className="detail-label">Estimated Cost:</span>
                    <span className="detail-value">{timeData.estimated_cost || 'Not specified'}</span>
                </div>
            </div>
        );
    };

    return (
        <div className="App">
            <div className="container">
                <div className="header">
                    <h1>🌍 AI Travel Itinerary Builder</h1>
                    <p>Create weather-aware travel plans powered by AI</p>
                </div>

                <div className="form-container">
                    <form onSubmit={handleSubmit}>
                        <div className="form-group">
                            <label htmlFor="destination">Destination City</label>
                            <input
                                type="text"
                                id="destination"
                                name="destination"
                                value={formData.destination}
                                onChange={handleInputChange}
                                placeholder="e.g., Paris, Tokyo, New York"
                                required
                            />
                        </div>
                        <div className="form-group">
                            <label htmlFor="date">Travel Date</label>
                            <input
                                type="date"
                                id="date"
                                name="date"
                                value={formData.date}
                                onChange={handleInputChange}
                                required
                            />
                        </div>
                        <button
                            type="submit"
                            className="submit-btn"
                            disabled={loading || !formData.destination || !formData.date}
                        >
                            {loading ? 'Creating Itinerary...' : 'Generate Itinerary'}
                        </button>
                    </form>
                </div>

                {error && (
                    <div className="error">
                        <strong>Error:</strong> {error}
                    </div>
                )}

                {loading && (
                    <div className="loading">
                        <div className="loading-spinner"></div>
                        <p>Generating your personalized travel itinerary...</p>
                        <p>This may take a few moments as we fetch weather data and create your plan.</p>
                    </div>
                )}

                {itinerary && (
                    <div className="itinerary-container">
                        <div className="itinerary-header">
                            <h2>Your Travel Itinerary</h2>
                            <p>{itinerary.destination} • {formatDate(itinerary.date)}</p>
                        </div>

                        {itinerary.weather_data && (
                            <div className="weather-info">
                                <h3>🌤️ Weather Forecast</h3>
                                <div className="weather-details">
                                    <div className="weather-item">
                                        <span>{itinerary.weather_data.temperature}°C</span>
                                        Temperature
                                    </div>
                                    <div className="weather-item">
                                        <span>{itinerary.weather_data.description}</span>
                                        Conditions
                                    </div>
                                    <div className="weather-item">
                                        <span>{itinerary.weather_data.humidity}%</span>
                                        Humidity
                                    </div>
                                    <div className="weather-item">
                                        <span>{itinerary.weather_data.wind_speed} m/s</span>
                                        Wind Speed
                                    </div>
                                </div>
                            </div>
                        )}

                        {itinerary.itinerary_data && (
                            <>
                                {renderTimeSection(itinerary.itinerary_data.morning, '🌅 Morning')}
                                {renderTimeSection(itinerary.itinerary_data.afternoon, '☀️ Afternoon')}
                                {renderTimeSection(itinerary.itinerary_data.evening, '🌆 Evening')}

                                {itinerary.itinerary_data.weather_notes && (
                                    <div className="weather-notes">
                                        <h4>🌦️ Weather Recommendations</h4>
                                        <p>{itinerary.itinerary_data.weather_notes}</p>
                                    </div>
                                )}

                                {itinerary.itinerary_data.total_estimated_cost && (
                                    <div className="total-cost">
                                        <h4>💰 Total Estimated Cost</h4>
                                        <div className="amount">{itinerary.itinerary_data.total_estimated_cost}</div>
                                    </div>
                                )}
                            </>
                        )}
                    </div>
                )}
            </div>
        </div>
    );
}

export default App; 