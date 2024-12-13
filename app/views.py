from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect
from .models import ToDo
from .forms import TodoForm
import json
from django.http import HttpResponse

@require_http_methods(["GET"])
@csrf_protect
def list_tasks(request):
    # Importar tareas
    if request.method == 'POST' and 'import_tasks' in request.FILES:
        try:
            file = request.FILES['import_tasks']
            tasks_data = json.load(file)

            # Opcional: Eliminar tareas existentes
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
    tasks = ToDo.objects.all()
    return render(request, 'index.html', {
        'tasks': tasks,
        'form': form
    })

@require_http_methods(["GET"])
def edit_task_get(request, task_id):
    """
    Maneja la carga del formulario de edición de una tarea.
    Solo acepta solicitudes GET.
    """
    task = get_object_or_404(ToDo, id=task_id)
    form = TodoForm(instance=task)
    return render(request, 'edit_task.html', {'form': form, 'task': task})


@require_http_methods(["POST"])
@csrf_protect
def edit_task_post(request, task_id):
    """
    Maneja la actualización de la tarea.
    Solo acepta solicitudes POST con protección CSRF.
    """
    task = get_object_or_404(ToDo, id=task_id)
    form = TodoForm(request.POST, instance=task)

    if form.is_valid():
        form.save()
        messages.success(request, 'Tarea actualizada exitosamente.')
        return redirect('list_tasks')

    # En caso de error, renderiza el formulario con los errores
    return render(request, 'edit_task.html', {'form': form, 'task': task})

@require_http_methods(["GET"])
def delete_task(request, task_id):
    task = get_object_or_404(ToDo, id=task_id)
    task.delete()
    messages.success(request, 'Tarea eliminada exitosamente.')
    return redirect('list_tasks')

@require_http_methods(["GET"])
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

@require_http_methods(["GET"])
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