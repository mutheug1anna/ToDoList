from django.shortcuts import render, redirect
from .models import Profile

def home(request):
    if request.method == 'POST':
        profile_name = request.POST.get('profile')
        if profile_name:
            Profile.objects.create(name=profile_name)
        return redirect('home')

    profiles = Profile.objects.all()
    return render(request, 'accounts/home.html', {'profiles': profiles})
