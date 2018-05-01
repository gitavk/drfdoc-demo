from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView)


from scenario.models import Scenario
from scenario.serializers import ScenarioSerializer


class ScenarioViewSet(ListAPIView, CreateAPIView, GenericViewSet):
    """
    List and Create operations with Scenario Model via ScenarioSerializer
    """
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer


class ScenarioDetailViewSet(RetrieveAPIView, DestroyAPIView, GenericViewSet):
    """
    Retrieve and Delete operations with Scenario Model via ScenarioSerializer
    """
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer
