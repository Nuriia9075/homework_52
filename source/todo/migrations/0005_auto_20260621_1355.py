from django.db import migrations


def create_default_project(apps, schema_editor):
    Project = apps.get_model('todo', 'Project')
    Task = apps.get_model('todo', 'Task')
    default_project = Project.objects.create(name="Project 1", created_at="2026-12-01")
    Task.objects.update(project=default_project)

def re_default_project(apps, schema_editor):
    Task = apps.get_model('todo', 'Task')
    Project = apps.get_model('todo', 'Project')

class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_project_task_project'),
    ]

    operations = [migrations.RunPython(create_default_project, re_default_project)
    ]
