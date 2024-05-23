from django.db import models
from users.models import User
from itens.models import Item

class Pedidos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedidos {self.id} by {self.user.full_name}"