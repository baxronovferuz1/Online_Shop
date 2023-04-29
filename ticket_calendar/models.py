from django.db import models
from events.models import Event, EventSession, Event, EventImage


class Calendar(models.Model):
    user_data=models.ForeignKey(Event, on_delete=models.CASCADE, null=False)
    consert_date=models.ForeignKey(EventSession, on_delete=models.CASCADE, null=False)
    corsert_image=models.ForeignKey(EventImage, on_delete=models.CASCADE, null=False)


    def __str__(self) -> str:
        return self.consert_image.image
