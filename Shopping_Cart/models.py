# Target for shopping cart

# 1)create Shopping_cart class
# status


from django.db import models
from django.contrib.auth.models import User
import product
import user_profile

class Shopping_Cart(models.Model):

    status_choice=(
        ("on_cart","on_cart"),
        ("ready_to_payment","ready_to_payment")
    )