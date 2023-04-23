# Target for shopping cart

# 1)create Shopping_cart class
# status


from django.db import models
from django.contrib.auth.models import User
import product
import user_profile
from product.models import BaseItem


class Shopping_Cart(models.Model):

    status_choice=(
        ("on_cart","on_cart"),
        ("ready_to_payment","ready_to_payment")
    )

    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    item=models.ForeignKey(BaseItem, on_delete=models.CASCADE, null=True)
    quantity=models.IntegerField(max_length=500)
    status=models.CharField(max_length=100, choices=status_choice, null=True)
    product = models.ForeignKey(BaseItem, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.item.name


    def total_price(self):
        return self.quantity * self.product.price