from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-weather/', views.add_weather, name='add_weather'),
    path('edit-weather/<int:pk>/', views.edit_weather, name='edit_weather'),
    path('delete-weather/<int:pk>/', views.delete_weather, name='delete_weather'),
]
