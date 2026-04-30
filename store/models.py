from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    category = models.CharField(max_length=100)
    prod_description = models.TextField()

    def __str__(self):
        return self.name