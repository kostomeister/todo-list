from django.shortcuts import render
from django.views import generic
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


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 10
