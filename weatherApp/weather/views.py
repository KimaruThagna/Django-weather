from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms  import WeatherForm,  


def data_retrieval(latitude, longitude):
    URL = f'https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={latitude}&lon={longitude}'
    
def weather_view(request):
     if request.method == 'POST':
            form = WeatherForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                latitide = data.get('latitide')
                longitude = data.get('longitude')
                # retrieve data from resource
                results = 1
                return render(request, "weather.html", {'form': form, 'results':results})
     else:
        form = WeatherForm() # blank form object just to pass context if not post method

        return render(request, "weather.html", {'form': form, 'results':None})
