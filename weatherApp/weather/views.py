from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms  import WeatherForm,  

def weather_view(request):
     if request.method == 'POST':
            form = WeatherForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                latitide = data.get('latitide')
                longitude = data.get('longitude')
                
            
                return HttpResponse("valid entiries")
            else:
                return HttpResponseRedirect('/')  # mention redirect url in argument
     else:
        form = WeatherForm() # blank form object just to pass context if not post method

        return render(request, "weather.html", {'form': form})
