from rest_framework.routers import DefaultRouter
from itens.api.viewsets import ItemViewSet

router = DefaultRouter()
router.register(r'itens', ItemViewSet, basename='itens')

urlpatterns = router.urls
