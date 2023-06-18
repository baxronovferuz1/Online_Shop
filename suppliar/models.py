from django.db import models
from user_profile.models import UserInformation, User
from Shopping_Cart.models import Shopping_Cart

# Create your models here.

# target

# create Class Suppliar check(yetkazib berishni tekshiradi)
# -status

# -phone number
# -status
# -addres
# -recipient(qabul qiluvchi)


class Suppliar_Check(models.Model):

    status_choices=(
        ("ready","Ready"),
        ("on_process","on_procces"),
    )

    phone_n=models.CharField(max_length=13)
    status=models.CharField(max_length=20, choices=status_choices)
    address=models.ForeignKey(UserInformation, on_delete=models.DO_NOTHING)
    recipient=models.ForeignKey(User, on_delete=models.CASCADE)
    factor=models.ForeignKey(Shopping_Cart, on_delete=models.CASCADE, null=True, blank=True)


