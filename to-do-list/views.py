from django.shortcuts import render


def tasks(request):
    context = {    
        "page_title": "Tasks",
        "user_name": "Wairia"
    }
    return render(request, "tasks.html", context)