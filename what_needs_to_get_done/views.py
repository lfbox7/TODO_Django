from django.views.generic import ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Task
from .forms import TaskForm



class TaskList(ListView):

    model: Task

    def get_queryset(self):
        return Task.objects.order_by('-due_date')


class TaskDetail(DetailView):
    model = Task


class TaskCreate(SuccessMessageMixin, CreateView):
    model: Task
    form_class = TaskForm
    success_url = reverse_lazy('task_list')
    success_message = 'Task successfully created!'


class TaskUpdate(SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task_list')
    success_message = 'Task successfully updated!'


class TaskDelete(SuccessMessageMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('task_list')
    success_message = 'Task successfully deleted!'