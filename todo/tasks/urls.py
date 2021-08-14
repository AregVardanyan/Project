from django.urls import path
from tasks import views

urlpatterns = [
    path("", views.get_home_page, name="home"),
    path("task_view/<int:task_id>", views.get_task, name="task-view"),
    path("new_task", views.create_task, name="new-task")
]