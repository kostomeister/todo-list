from django import forms

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


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
