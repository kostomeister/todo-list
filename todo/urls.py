from django.urls import path

from todo.views import TaskListView, TaskDetailView, TagListView, TagDetailView, TaskCreateView, TaskUpdateView, \
    TagUpdateView, TagCreateView, TaskDeleteView, TagDeleteView, do_task_view, undo_task_view, DoneTaskListView, \
    UnDoneTaskListView

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("done/", DoneTaskListView.as_view(), name="task-done"),
    path("undone/", UnDoneTaskListView.as_view(), name="task-undone"),
    path("<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("<int:pk>/do/", do_task_view, name="task-do"),
    path("<int:pk>/undo/", undo_task_view, name="task-undo"),
    path("task-create/", TaskCreateView.as_view(), name="task-create"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/<int:pk>/", TagDetailView.as_view(), name="tag-detail"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "todo"
