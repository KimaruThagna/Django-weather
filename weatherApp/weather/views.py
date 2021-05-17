import requests
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms  import WeatherForm


def data_retrieval(latitude, longitude):
    URL = f'https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={latitude}&lon={longitude}'
    results = requests.get(URL) # getting a forbidden error here
    # in the interest of time, I have assumed a json response and considered the below structure as seen in the browser
    data = results.json()
    return data['properties']['units']

def weather_view(request):
     if request.method == 'POST':
            form = WeatherForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                latitude = data.get('latitide')
                longitude = data.get('longitude')
                # retrieve data from resource
                results = data_retrieval(latitude,longitude)
                print(results)
                return render(request, "weather/weather.html", {'form': form, 'results':results})
     else:
        form = WeatherForm() # blank form object just to pass context if not post method

        return render(request, "weather/weather.html", {'form': form, 'results':None})
