from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from .forms import TaskForm, TagForm
from .models import Task, Tag


class TaskListView(generic.ListView):
    model = Task

    def get_queryset(self):
        return Task.objects.prefetch_related("tags")


class DoneTaskListView(generic.ListView):
    model = Task
    template_name = "todo/task_list.html"

    def get_queryset(self):
        return Task.objects.prefetch_related("tags").filter(is_done=True)


class UnDoneTaskListView(generic.ListView):
    model = Task
    template_name = "todo/task_list.html"

    def get_queryset(self):
        return Task.objects.prefetch_related("tags").filter(is_done=False)


class TaskDetailView(generic.DetailView):
    model = Task

    def get_queryset(self):
        return Task.objects.prefetch_related("tags")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("todo:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("todo:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:index")


def do_task_view(request: HttpRequest, pk: int) -> HttpResponse:
    task = get_object_or_404(Task, pk=pk)
    task.is_done = True
    task.save()
    return redirect(request.META.get('HTTP_REFERER'))


def undo_task_view(request: HttpRequest, pk: int) -> HttpResponse:
    task = get_object_or_404(Task, pk=pk)
    task.is_done = False
    task.save()
    return redirect(request.META.get('HTTP_REFERER'))


class TagListView(generic.ListView):
    model = Tag


class TagDetailView(generic.DetailView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")
