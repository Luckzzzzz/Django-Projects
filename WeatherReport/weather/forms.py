from django import forms
from .models import Weather

class WeatherForm(forms.ModelForm):
    class Meta:
        model = Weather
        fields = ['city', 'temperature', 'condition', 'humidity', 'wind_speed']
