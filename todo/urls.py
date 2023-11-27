from django.urls import path

from todo.views import TaskListView, TaskDetailView, TagListView, TagDetailView, TaskCreateView, TaskUpdateView, \
    TagUpdateView, TagCreateView, TaskDeleteView, TagDeleteView

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("task-create/", TaskCreateView.as_view(), name="task-create"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/<int:pk>/", TagDetailView.as_view(), name="tag-detail"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/delete/", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "todo"
