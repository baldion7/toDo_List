from django.urls import path
from . import views

urlpatterns = [
    path('',  views.list_tasks_get, name='list_tasks'),  # Para listar tareas
    path('import/',  views.import_tasks, name='import_tasks'),  # Para importar tareas
    path('create/',  views.create_task_post, name='create_task_post'),  # Para crear tareas
    path('edit/<int:task_id>/', views.edit_task_get, name='edit_task_get'),  # Para solicitudes GET
    path('edit_task/<int:task_id>/', views.edit_task_post, name='edit_task_post'),  # Para solicitudes POST
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('export/', views.export_tasks, name='export_tasks'),
    path('change_status/<int:task_id>/', views.change_task_status, name='change_task_status'),
]
