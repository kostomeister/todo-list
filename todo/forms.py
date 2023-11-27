from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from todo.models import Tag, Task


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            'deadline': forms.TextInput(attrs={'type': 'datetime-local'}),
        }

    def clean_deadline(self):
        deadline = self.cleaned_data.get('deadline')
        now = timezone.now()

        if deadline and deadline < now:
            raise ValidationError('Deadline must be not less than current date')

        return deadline

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
