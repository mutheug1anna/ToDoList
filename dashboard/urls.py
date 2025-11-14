from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard_view, name='dashboard_page'),
    path('tasks/', views.tasks_list, name='tasks_list'),
    path('users/', views.users_list, name='users_list'),
    path('notifications/', views.notifications_list, name='notifications_list'),
    path('projects/', views.projects_list, name='projects_list'),
]
