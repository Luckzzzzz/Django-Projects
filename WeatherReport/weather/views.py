from django.shortcuts import render, redirect, get_object_or_404
from .models import Weather
from .forms import WeatherForm

def home(request):
    weather_data = Weather.objects.all()
    return render(request, 'weather/home.html', {'weather_data': weather_data})

def add_weather(request):
    if request.method == 'POST':
        form = WeatherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = WeatherForm()
    return render(request, 'weather/add_weather.html', {'form': form})

def edit_weather(request, pk):
    weather = get_object_or_404(Weather, pk=pk)
    if request.method == 'POST':
        form = WeatherForm(request.POST, instance=weather)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = WeatherForm(instance=weather)
    return render(request, 'weather/edit_weather.html', {'form': form, 'weather': weather})

def delete_weather(request, pk):
    weather = get_object_or_404(Weather, pk=pk)
    if request.method == 'POST':
        weather.delete()
        return redirect('home')
    return render(request, 'weather/delete_weather.html', {'weather': weather})
