from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from todo.models import Task, Tag


class TaskCreateViewTest(TestCase):
    def test_task_create_view(self):
        task_count_before = Task.objects.count()
        deadline = timezone.now() + timezone.timedelta(days=1)
        tag1 = Tag.objects.create(name="Test Tag1")
        tag2 = Tag.objects.create(name="Test Tag2")
        response = self.client.post(reverse('todo:task-create'), data={
            'content': 'Test Task',
            'deadline': deadline,
            "is_done": False,
            'tags': [tag1.id, tag2.id],
        })
        task_count_after = Task.objects.count()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(task_count_after, task_count_before + 1)

    def test_task_create_view_no_tags(self):
        task_count_before = Task.objects.count()
        deadline = timezone.now() + timezone.timedelta(days=1)
        response = self.client.post(reverse('todo:task-create'), data={
            'content': 'Test Task',
            'deadline': deadline,
            'tags': [],
        })
        task_count_after = Task.objects.count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(task_count_after, task_count_before)


class TagCreateViewTest(TestCase):
    def test_tag_create_view(self):
        tag_count_before = Tag.objects.count()
        response = self.client.post(reverse('todo:tag-create'), data={
            'name': 'Test Tag',
        })
        tag_count_after = Tag.objects.count()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(tag_count_after, tag_count_before + 1)

    def test_tag_create_view_invalid_data(self):
        tag_count_before = Tag.objects.count()
        response = self.client.post(reverse('todo:tag-create'), data={
            'name': '',
        })
        tag_count_after = Tag.objects.count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(tag_count_after, tag_count_before)
