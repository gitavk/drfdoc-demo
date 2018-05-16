from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView,
    DestroyAPIView)


from scenario.models import Scenario
from scenario.serializers import ScenarioSerializer


class ScenarioViewSet(ListAPIView, CreateAPIView, GenericViewSet):
    """
    List and Create operations with Scenario Model via ScenarioSerializer
    """
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer


class ScenarioDetailViewSet(
        RetrieveAPIView, UpdateAPIView, DestroyAPIView, GenericViewSet
        ):
    """
    Retrieve, Update and Delete operations with Scenario Model via ScenarioSerializer
    """
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer
