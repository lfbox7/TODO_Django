from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    def __init_subclass__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs = {
            'class': 'form-control col-6'
        }
        self.fields['due_date'].widget.attrs = {
            'class': 'form-control col-6'
        }
        self.fields['status'].widget.attrs = {
            'class': 'form-control col-6'
        }

    class Meta:
        model = Task
        fields = ('title', 'due_date', 'status')