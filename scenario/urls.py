from rest_framework import routers


from .views import TaskViewSet, TaskDetailViewSet
from .views import ScenarioViewSet, ScenarioDetailViewSet


router = routers.SimpleRouter()
router.register(r'task', TaskViewSet)
router.register(r'task', TaskDetailViewSet)
router.register(r'scenario', ScenarioViewSet)
router.register(r'scenario', ScenarioDetailViewSet)
urlpatterns = router.urls