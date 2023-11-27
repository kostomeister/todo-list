from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import TaskForm, TagForm
from .models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 7

    def get_queryset(self):
        return Task.objects.prefetch_related("tags")


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


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 10


class TagDetailView(generic.DetailView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("todo:tag-list")
