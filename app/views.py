from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import ToDo
from .forms import TodoForm
import json
from django.http import JsonResponse, HttpResponse


def list_tasks(request):
    # Manejar la importación de tareas
    if request.method == 'POST' and 'import_tasks' in request.FILES:
        try:
            file = request.FILES['import_tasks']
            tasks_data = json.load(file)

            # Eliminar tareas existentes (opcional)
            ToDo.objects.all().delete()

            # Crear nuevas tareas desde el archivo
            for task_data in tasks_data:
                ToDo.objects.create(
                    title=task_data.get('title', ''),
                    description=task_data.get('description', ''),
                    status=task_data.get('status', 'pendiente')
                )

            messages.success(request, 'Tareas importadas exitosamente.')
            return redirect('list_tasks')
        except Exception as e:
            messages.error(request, f'Error al importar tareas: {str(e)}')

    # Crear nueva tarea
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Tarea creada exitosamente.')
        return redirect('list_tasks')

    # Listar tareas
    tasks = ToDo.objects.all().order_by('-created_at')
    return render(request, 'index.html', {
        'tasks': tasks,
        'form': form
    })


def edit_task(request, task_id):
    task = get_object_or_404(ToDo, id=task_id)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarea actualizada exitosamente.')
            return redirect('list_tasks')
    else:
        form = TodoForm(instance=task)

    return render(request, 'edit_task.html', {'form': form, 'task': task})


def delete_task(request, task_id):
    task = get_object_or_404(ToDo, id=task_id)
    task.delete()
    messages.success(request, 'Tarea eliminada exitosamente.')
    return redirect('list_tasks')


def export_tasks(request):
    # Exportar todas las tareas a JSON
    tasks = ToDo.objects.all()
    tasks_data = [
        {
            'title': task.title,
            'description': task.description,
            'status': task.status,
            'created_at': task.created_at.isoformat(),
            'updated_at': task.updated_at.isoformat()
        } for task in tasks
    ]

    response = HttpResponse(
        json.dumps(tasks_data, indent=4),
        content_type='application/json'
    )
    response['Content-Disposition'] = 'attachment; filename=tareas_exportadas.json'
    return response


def change_task_status(request, task_id):
    task = get_object_or_404(ToDo, id=task_id)

    # Ciclo de estados
    status_cycle = {
        'pendiente': 'en_proceso',
        'en_proceso': 'completado',
        'completado': 'cancelado',
        'cancelado': 'pendiente'
    }

    task.status = status_cycle.get(task.status, 'pendiente')
    task.save()

    messages.success(request, f'Estado de la tarea actualizado a {task.get_status_display()}.')
    return redirect('list_tasks')
