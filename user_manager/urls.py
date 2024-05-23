from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from users.api import viewsets as usersviewsets
from itens.api import viewsets as itensviewsets
from pedidos.api import viewsets as pedidosviewsets

route = routers.DefaultRouter()

route.register(r'users', usersviewsets.UserViewSet, basename="Users") 
route.register(r'pedidos', pedidosviewsets.PedidosViewSet, basename="Pedidos") 
route.register(r'itens', itensviewsets.ItemViewSet, basename="Itens") 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    path('api/', include('itens.api.urls')),
    path('api/', include('pedidos.api.urls')),
]
