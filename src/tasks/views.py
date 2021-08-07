from django.shortcuts import get_object_or_404, redirect, render

from .forms import TaskModelForm
from .models import Task


def task_list_view(request):
    """Renders two lists: completed and incomplete tasks."""
    form = TaskModelForm()
    if request.method == 'POST':
        form = TaskModelForm(request.POST or None)
        if form.is_valid:
            form.save()
            return redirect('task-list')

    task_list = Task.objects.filter(completed=False)
    completed_list = Task.objects.filter(completed=True)
    context = {
        'task_list': task_list,
        'completed_list': completed_list,
        'form': form,
    }
    return render(request, 'task_list.html', context)


def toggle_task_status(request, id):
    """Toggles the task status (completed or incomplete)."""
    task = get_object_or_404(Task, id=id)
    task.completed = not task.completed
    task.save()


def complete_task(request, id):
    """Marks the task as completed."""
    toggle_task_status(request, id)
    return redirect('task-list')


def recover_task(request, id):
    """Marks the task as incomplete."""
    toggle_task_status(request, id)
    return redirect('task-list')


def toggle_task_completion(request, id):
    """Toggles the task status: whether the task completed or incomplete."""
    task = get_object_or_404(Task, id=id)
    task.completed = not task.completed
    task.save()
    return redirect('task-list')


def delete_task(request, id):
    """Deletes the task."""
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('task-list')
