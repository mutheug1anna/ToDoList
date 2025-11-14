from django.urls import path
from django.contrib.auth import views as auth_views
from . import views # Import views from the accounts app

urlpatterns = [
    # Home Page for the root URL
    path('', views.home, name='home'), 

    # Django's built-in authentication URLs
    # Template name is now simpler: 'accounts/login.html'
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    
    # Logout path remains the same
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('signup/', views.signup, name='signup'),  # <-- name must match 'signup'

    # You will add register, password reset, etc., here later.
]