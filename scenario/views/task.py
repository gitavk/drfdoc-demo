from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView)


from scenario.models import Task
from scenario.serializers import TaskSerializer


class TaskViewSet(ListAPIView, CreateAPIView, GenericViewSet):
    """
    List and Create operations with Task Model via TaskSerializer
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetailViewSet(RetrieveAPIView, DestroyAPIView, GenericViewSet):
    """
    Retrieve and Delete operations with Task Model via TaskSerializer
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
