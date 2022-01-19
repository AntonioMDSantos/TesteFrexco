from django.db import models
from uuid import uuid4

# Create your models here.


class Regions(models.Model):
    name = models.CharField(max_length=50)

