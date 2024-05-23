from rest_framework.routers import DefaultRouter
from pedidos.api.viewsets import PedidosViewSet

router = DefaultRouter()
router.register(r'pedidos', PedidosViewSet, basename='Pedidos')

urlpatterns = router.urls
