from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_tasks, name='list_tasks'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('export/', views.export_tasks, name='export_tasks'),
    path('change_status/<int:task_id>/', views.change_task_status, name='change_task_status'),
]