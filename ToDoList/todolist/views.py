from django.shortcuts import render, redirect, get_object_or_404
from .models import Task 

#Create task
def task_list(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
        return redirect('task_list')

    tasks = Task.objects.all().order_by('complete', '-created')
    context = {'tasks': tasks}
    return render(request, 'task_list.html', context)

#Toggle Task 
def toggle_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.complete = not task.complete
        task.save()
    return redirect('task_list')

# Update Task 
def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_title = request.POST.get('title')
        if new_title:
            task.title = new_title
            task.save()
    return redirect('task_list')

#Delete Task 
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
    return redirect('task_list')