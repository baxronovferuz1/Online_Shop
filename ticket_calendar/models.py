from django.db import models


class Calendar(models.Model):
    user_data=models.ForeignKey()
