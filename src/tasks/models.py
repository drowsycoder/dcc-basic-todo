from django.db import models
from django.urls import reverse

LABEL_CHOICES = (
    ('P', 'primary'),
    ('SE', 'secondary'),
    ('S', 'success'),
    ('D', 'danger'),
    ('W', 'warning'),
    ('I', 'info'),
    ('L', 'light'),
    ('D', 'dark'),
)


class Task(models.Model):
    """Task model."""
    title = models.CharField(max_length=100)
    due_date = models.DateTimeField()
    label = models.CharField(choices=LABEL_CHOICES, max_length=2, default='P')
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_complete_task_url(self):
        """Returns URL for task completion function."""
        return reverse('complete-task', kwargs={'id': self.id})

    def get_recover_task_url(self):
        """Returns URL for task recovering function."""
        return reverse('recover-task', kwargs={'id': self.id})

    def get_delete_task_url(self):
        """Returns URL for task deletion function."""
        return reverse('delete-task', kwargs={'id': self.id})
