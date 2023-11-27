from django.urls import path

from todo.views import TaskListView, TaskDetailView

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("/<int:pk>/", TaskDetailView.as_view(), name="task-detail")
]

app_name = "todo"
