# Generated by Django 3.2.6 on 2021-08-07 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_task_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='label',
            field=models.CharField(choices=[('P', 'primary'), ('SE', 'secondary'), ('S', 'success'), ('D', 'danger'), ('W', 'warning'), ('I', 'info'), ('L', 'light'), ('D', 'dark')], default='P', max_length=2),
        ),
    ]
