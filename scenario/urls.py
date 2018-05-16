from django.conf.urls import url

from rest_framework import routers


from .views import ProductViewSet
from .views import TaskViewSet, TaskDetailViewSet
from .views import ScenarioViewSet, ScenarioDetailViewSet


router = routers.SimpleRouter()
router.register(r'task', TaskViewSet)
router.register(r'task', TaskDetailViewSet)
router.register(r'scenario', ScenarioViewSet)
router.register(r'scenario', ScenarioDetailViewSet)

urlpatterns = router.urls + [
    url(r'^products/uuid/(?P<uuid>[^/.]+)/',
        ProductViewSet.as_view(), name='product-retrieve-uuid'),
    url(r'^products/(?P<pk>[^/.]+)/',
        ProductViewSet.as_view(), name='product-retrieve'),
]
