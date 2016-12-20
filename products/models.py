from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    stock = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name

    @property
    def is_stocked(self):
        if self.stock:
            return True
        return False

class CartProduct(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    cart = models.ForeignKey('user_auth.Cart')
    description = models.TextField()

    def __str__(self):
        return str(self.name + self.cart.user.username)
