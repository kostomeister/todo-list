from django.urls import path

from todo.views import TaskListView, TaskDetailView, TagListView, TagDetailView

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/<int:pk>/", TagDetailView.as_view(), name="tag-detail")
]

app_name = "todo"
