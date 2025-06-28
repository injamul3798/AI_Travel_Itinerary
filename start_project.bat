@echo off
echo ========================================
echo    AI Travel Itinerary Builder
echo ========================================
echo.

echo Starting Backend Server...
echo.
cd backend
start "Django Backend" cmd /k "python manage.py runserver"
echo Backend server starting on http://127.0.0.1:8000
echo.

echo Starting Frontend Server...
echo.
cd ../frontend
start "React Frontend" cmd /k "npm start"
echo Frontend server starting on http://localhost:3000
echo.

echo ========================================
echo    Both servers are starting...
echo ========================================
echo.
echo Backend:  http://127.0.0.1:8000
echo Frontend: http://localhost:3000
echo Admin:    http://127.0.0.1:8000/admin
echo.
echo Press any key to close this window...
pause > nul 