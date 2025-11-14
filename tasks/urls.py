from django.urls import path,include
from . import views

urlpatterns = [
    # path("", include('tasks.urls')),
    path('', views.tasks, name='tasks'), 
    path("add/", views.add_task, name='add_task'),
    path("view/", views.taskview, name='taskview'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('toggle_complete/<int:task_id>/', views.toggle_complete, name='toggle_complete'),
]
