from rest_framework import serializers
from .models import Grocery

class GrocerySerializers(serializers.ModelSerializer):
    class Meta:
        model = Grocery
        fields = ['name', 'price']