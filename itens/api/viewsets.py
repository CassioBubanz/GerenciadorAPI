from rest_framework import viewsets
from itens.api import serializers
from itens import models

class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ItemSerializer
    queryset = models.Item.objects.all()