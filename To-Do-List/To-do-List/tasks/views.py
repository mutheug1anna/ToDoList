from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Task

# Create your views here.
def tasks(request):
    # todolist = ["Read book", "Complete project", "Buy groceries"]
    todolist = Task.objects.all().order_by('dueDate')
    # context = {
    #     "page_title": "To-Do List",
    #     "user_name": "Me",
    #     "todolist": todolist,
    # }
    # return render(request, 'tasks.html', context)
    return render(request, 'tasks.html', {
        "page_title": "To-Do List",
        "user_name": "User",
        "todolist": todolist,
    })

# def tasks(request):
#     todolist = Task.objects.all()  # ensures all have valid IDs
#     return render(request, 'tasks.html', {'todolist': todolist})

# New view for adding a task
def add_task(request):
    if request.method == 'POST':
        task_name = request.POST.get('task')
        duration = request.POST.get('duration')
        due_date = request.POST.get('dueDate')
        print(f"Task: {task_name}, {duration}, Due: {due_date}")  
        
        if task_name and due_date:
            Task.objects.create(
                name=task_name, 
                duration=int(duration),
                dueDate=due_date)
        
        return redirect('taskview')  # Go back to task list
    else:
        return redirect('tasks')
    
# def taskview(request):
#     todolist = Task.objects.all().order_by('name', 'duration', 'dueDate')
#     return render(request, 'tasks/taskview.html', {
#         'todolist': todolist,
#         'user_name': 'User'
#     })
    
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('tasks')

def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if request.method == 'POST':
        task_name = request.POST.get('task')
        duration = request.POST.get('duration')
        due_date = request.POST.get('dueDate')
        # task.save()
        # return redirect('tasks')
    
        if task_name and duration and due_date:
            task.name = task_name
            task.duration = duration
            task.dueDate = due_date
            task.save()
            return redirect('tasks')
        else:
            return render(request, 'tasks/edit_task.html', {
                'task': task,
                'error': 'All fields are required'
            })

    return render(request, 'edit_task.html', {'task': task})

def toggle_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('tasks')

def taskview(request):
    tasks = Task.objects.all()

    # Filtering
    status = request.GET.get('status')
    if status == 'completed':
        tasks = tasks.filter(completed=True)
    elif status == 'pending':
        tasks = tasks.filter(completed=False)

    # Sorting
    sort = request.GET.get('sort')
    if sort == 'dueDate':
        tasks = tasks.order_by('dueDate')
    elif sort == 'duration':
        tasks = tasks.order_by('duration')

    return render(request, 'tasks/taskview.html', {'tasks': tasks})
