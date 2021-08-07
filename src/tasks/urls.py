from django.urls import path

from tasks.views import delete_task, task_list_view, toggle_task_completion

urlpatterns = [
    path(
        '<id>/toggle-task-completion/',
        toggle_task_completion,
        name='toggle-task-completion'
    ),
    path('<id>/delete-task/', delete_task, name='delete-task'),
    path('', task_list_view, name='task-list')
]
