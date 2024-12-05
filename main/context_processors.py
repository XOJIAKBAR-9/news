import requests
from random import choice
from datetime import datetime
from .models import *

def base_context(request):
    # Get top 5 random articles
    base_top5_random_articles = Article.objects.filter(published=True).order_by("-views")[:5]
    base_top5_random_articles = choice(base_top5_random_articles) if base_top5_random_articles else None

    # Get the current weekday
    hafta_kunlari = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    hafta_kuni = hafta_kunlari[datetime.now().weekday()]

    # Fetch weather data
    try:
        response = requests.get(
            'https://api.weatherapi.com/v1/current.json?q=Fergana&key=3eead9e64e5248bcbf8112613241811'
        )
        if response.status_code == 200:
            weather_data = response.json()  # Parse JSON response
            temperature = {
                "temp_c": weather_data.get('current', {}).get('temp_c'),
                "location": weather_data.get('location', {}).get('name'),
                "icon": weather_data.get('current', {}).get('condition', {}).get('icon'),
            }
        else:
            temperature = {"error": "Failed to fetch weather data"}
    except requests.RequestException as e:
        temperature = {"error": f"An error occurred: {str(e)}"}

    # Construct context
    context = {
        'base_top5_random_articles': base_top5_random_articles,
        'weekday': hafta_kuni,
        'today': str(datetime.today().strftime("%d-%m-%Y")).replace("-", "."),
        "temperature": temperature,
    }
    return context
