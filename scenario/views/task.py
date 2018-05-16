from django.utils.functional import cached_property

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

    @cached_property
    def user(self):
        return self.request.user

    def retrieve(self, *args, **kwargs):
        print(self.user)
        return super().retrieve(*args, **kwargs)
