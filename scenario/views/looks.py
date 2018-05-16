from django.shortcuts import get_object_or_404
from rest_framework import generics

from scenario.models import Task
from scenario.serializers import TaskSerializer


class ProductViewSet(generics.RetrieveAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        obj = get_object_or_404(queryset, **self.kwargs)  # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj
