from django.test import TestCase
from django.utils import timezone

from todo.forms import TaskForm, TagForm
from todo.models import Tag


class TaskFormTest(TestCase):
    def setUp(self):
        self.tag1 = Tag.objects.create(name="Test Tag1")
        self.tag2 = Tag.objects.create(name="Test Tag2")

    def test_clean_deadline_past_date(self):
        past_date = timezone.now() - timezone.timedelta(days=1)
        form_data = {
            "content": "Test Task",
            "deadline": past_date,
            "tags": [self.tag1.id, self.tag2.id],
        }
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("deadline", form.errors)
        self.assertEqual(
            form.errors["deadline"][0], "Deadline must be not less than current date"
        )

    def test_clean_deadline_current_date(self):
        current_date = timezone.now() + timezone.timedelta(minutes=10)
        form_data = {
            "content": "Test Task",
            "deadline": current_date,
            "tags": [self.tag1.id, self.tag2.id],
        }
        form = TaskForm(data=form_data)
        print(form.errors)
        self.assertTrue(form.is_valid())


class TagFormTest(TestCase):
    def test_tag_form_valid(self):
        form_data = {
            'name': 'Test Tag',
        }
        form = TagForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_tag_form_invalid_blank_name(self):
        form_data = {
            'name': '',
        }
        form = TagForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
        self.assertEqual(
            form.errors['name'][0],
            'This field is required.'
        )
