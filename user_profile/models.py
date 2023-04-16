from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

# target
# 1)UserInformation
#     *address
# 2)UserProfile
#     *(user,phone_number,address,is_verified,verification_uuid)


class UserInformation(models.Model):
    address=models.CharField(max_length=25)


    def __str__(self) -> str:
        return self.address
    
class UserProfile(models.Model):
    user=models.OneToOneField(User, related_name="users", on_delete=models.CASCADE)
    phone=models.CharField(max_length=25)
    address=models.ManyToManyField(UserInformation, related_name="informations", related_query_name="information")
    is_verified=models.BooleanField(default=False)
    verification_uuid=models.UUIDField("Unique Verification UUID", default=uuid.uuid4)


    def __str__(self) -> str:
        return self.user.username
