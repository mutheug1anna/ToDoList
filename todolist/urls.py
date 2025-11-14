from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin site URL
    path('admin/', admin.site.urls),

    # Route all requests for the accounts/auth pages
    # and the root path ('') to the accounts app's urls.py
    path('', include('accounts.urls')), 
    
    # Route for the dashboard app
    path('dashboard/', include('dashboard.urls')),

    # Route for notifications (adjust if needed, but keeping for now)
    # The current error suggests your project had this line:
    # path('dashboard/notifications/', include('notifications.urls')),
    # If the above line is in your file, keep it. 
    # Otherwise, you should place your notifications path here.
    path('tasks/', include('tasks.urls')),
]