from django.shortcuts import render

# Dashboard home view
def dashboard_view(request):
    return render(request, 'dashboard.html')

# Existing views
def tasks_list(request):
    return render(request, 'tasks.html')

def users_list(request):
    return render(request, 'users.html')

def notifications_list(request):
    return render(request, 'notifications.html')

def projects_list(request):
    return render(request, 'projects.html')
