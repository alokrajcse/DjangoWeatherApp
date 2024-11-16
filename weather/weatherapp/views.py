import requests
from django.shortcuts import render

def home(request):
    if request.method == "POST":
        city = request.POST['city']
        api_key = 'a62b49f7ea3949e29cb62131240707'  # Replace with your WeatherAPI key
        url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no'

        response = requests.get(url)
        data = response.json()

        if 'error' not in data:
            weather = {
                'city': data['location']['name'],
                'country': data['location']['country'],
                'temperature': data['current']['temp_c'],
                'condition': data['current']['condition']['text'],
                'icon': data['current']['condition']['icon'],
            }
        else:
            weather = None
    else:
        weather = None

    return render(request, 'home.html', {'weather': weather})
