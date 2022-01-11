from django.urls import path
from . import views

app_name = 'fyp'

urlpatterns = [
    path('', views.welcome, name='fyp-welcome'),
    
    
]