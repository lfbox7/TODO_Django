from django.urls import path
from . import views


urlpatterns = [
    path('', views.TaskList.as_view(), name='task_list'),
    path('view/<int:pk>', views.TaskDetail.as_view(), name='task_view'),
    path('new', views.TaskCreate.as_view(), name='task_new'),
    path('edit/<int:pk>/', views.TaskUpdate.as_view(), name='task_edit'),
    path('delete/<int:pk>/', views.TaskDelete.as_view(), name='task_delete'),
]