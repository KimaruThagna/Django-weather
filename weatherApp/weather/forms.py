from django import forms

class WeatherForm(forms.Form):

    latitude = forms.FloatField()
    longitude = forms.FloatField()