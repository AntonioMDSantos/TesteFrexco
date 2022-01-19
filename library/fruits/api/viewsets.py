from rest_framework import viewsets
from fruits.api import serializers
from fruits import models

class FruitsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FruitsSerializer
    queryset = models.Fruits.objects.all()