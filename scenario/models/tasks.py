"""
The model and help methods for Task
"""
import uuid

from django.db import models
from django.conf import settings


class Task(models.Model):
    """
    Description of the model,
    attr project was comment to create a working version of the application
    """
    stakeholder = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='tasks', blank=True,
        on_delete=None)
    # project = models.ForeignKey(Project, related_name='project_tasks' )
    title = models.CharField(max_length=50, blank=True, null=True, )
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
