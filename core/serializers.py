from rest_framework import serializers
from .models import Grocery


class GrocerySerializers(serializers.ModelSerializer):
    description = serializers.CharField(required=False)

    class Meta:
        model = Grocery
        fields = ['name', 'price', 'description']
