from rest_framework import serializers
from fruits import models

class FruitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fruits
        fields = '__all__'