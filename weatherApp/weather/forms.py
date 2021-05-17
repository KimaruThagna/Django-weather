from django import forms

class MyForm(forms.Form):
    
    latitude = forms.FloatField()
    longitude = forms.FloatField()