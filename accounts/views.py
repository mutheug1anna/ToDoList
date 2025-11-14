from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# This view will use the globally placed home.html template
def home(request):
    # Check if the user is authenticated (logged in)
    if request.user.is_authenticated:
        # If logged in, redirect them immediately to the dashboard
        return redirect('dashboard:dashboard_page')
    else:
        # If not logged in, show the landing page
        return render(request, 'home.html') # Now looking for ToDoList/templates/home.html
    
# Signup view
def signup(request):
    if request.user.is_authenticated:
        return redirect('dashboard:dashboard_page')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect('login')  # Make sure you have a URL named 'login'
    else:
        form = UserCreationForm()
    
    return render(request, 'accounts/signup.html', {'form': form})