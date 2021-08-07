from django.urls import path

from tasks.views import (complete_task, delete_task, recover_task,
                         task_list_view)

urlpatterns = [
    path('<id>/complete-task/', complete_task, name='complete-task'),
    path('<id>/recover-task/', recover_task, name='recover-task'),
    path('<id>/delete-task/', delete_task, name='delete-task'),
    path('', task_list_view, name='task-list')
]
