"""
The model and help methods for Task
"""
from django.db import models
from django.conf import settings


class Scenario(models.Model):
    """
    Description of the model,
    attr project was comment to create a working version of the application
    """
    stakeholder = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='scenarios', blank=True,)
    tasks = models.ManyToManyField('scenario.Task', blank=True)
