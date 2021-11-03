import uuid
from django.db import models
import jsonfield


# Create your models here.
class VehicleMod(models.Model):
    speed = models.IntegerField(default=0)
    avg_speed = models.IntegerField(default=0)
    temperature = models.IntegerField(default=0)
    fuel_level = models.IntegerField(default=0)
    engine_status = jsonfield.JSONField(default=dict)
    latitude = models.FloatField(default=0.00)
    longitude = models.FloatField(default=0.00)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return "%s" % self.id
