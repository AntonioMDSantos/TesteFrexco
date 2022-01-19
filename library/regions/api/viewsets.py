from rest_framework import viewsets
from regions.api import serializers
from regions import models

class RegionsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RegionsSerializer
    queryset = models.Regions.objects.all()