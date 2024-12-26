import requests
from django.shortcuts import render

def weather(request):
    city = request.GET.get('city', 'Hamburg')  # Default city
    weather_data = None

    if city:
        # Replace with your OpenWeatherMap API key
        api_key = "762c1d5e1b8143414f490d3b1ac8b41d"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                "city": city,
                "temperature": data['main']['temp'],
                "feels_like": data['main']['feels_like'],
                "humidity": data['main']['humidity'],
                "description": data['weather'][0]['description'],
                "wind_speed": data['wind']['speed']
            }

    return render(request, 'weather_app/index.html', {'weather_data': weather_data})
