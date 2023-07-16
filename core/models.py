from django.db import models


class Grocery(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)
    price = models.FloatField(max_length=50)
    description = models.TextField()
# Create your models here.
