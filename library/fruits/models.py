from django.db import models
from uuid import uuid4

from regions.models import Regions

# Create your models here.

class Fruits(models.Model):
    name = models.CharField(max_length=50)
    region = models.ForeignKey(Regions, on_delete=models.CASCADE, related_name="fruits")