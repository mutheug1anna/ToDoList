from django.urls import path
from . import views  # Import the notifications_page view

urlpatterns = [
    path('', views.notifications_page, name='notifications_page'),
]
