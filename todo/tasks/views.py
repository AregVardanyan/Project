from django.shortcuts import render
from .models import Task


def get_home_page(request):
    tasks = Task.objects.all()
    return render(request, "tasks/home.html", {"task_list": tasks})


def get_task(request, task_id):
    task_object = Task.objects.get(id=task_id)
    contex = {
        "task_id": task_id,
        "task_object": task_object
    }
    return render(request, "tasks/task_view.html", contex, )


def create_task(request):
    return render(request, "tasks/new_task.html")
