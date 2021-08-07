from django.shortcuts import get_object_or_404, redirect, render

from .forms import TaskModelForm
from .models import Task


def task_list_view(request):
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


def complete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.completed = True
    task.save()
    return redirect('task-list')


def recover_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.completed = False
    task.save()
    return redirect('task-list')


def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('task-list')
