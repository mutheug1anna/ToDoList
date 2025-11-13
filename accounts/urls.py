from django.urls import path
from . import views

urlpatterns = [
    # Home page showing all tasks
    path('', views.home, name='home'),

    
]
