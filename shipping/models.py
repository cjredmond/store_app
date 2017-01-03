from django.db import models
from django.contrib.auth.models import User

class Shipment(models.Model):
    user = models.ForeignKey('auth.User')

    @property
    def items(self):
        return self.orderproduct_set.all()

    def total(self):
        return round(sum([product.price for product in self.items]),2)

class OrderProduct(models.Model):
    shipment = models.ForeignKey(Shipment)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()
    
