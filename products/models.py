from django.db import models
from django.db.models import IntegerField
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime, timezone, timedelta

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

    def all_reviews(self):
        return self.review_set.all()

class Review(models.Model):
    user = models.ForeignKey('auth.User')
    text = models.TextField()
    product = models.ForeignKey(Product)
    time = models.DateTimeField(auto_now_add=True)
    rating = IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)])
    class Meta:
        unique_together = ('user', 'product')

class CartProduct(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    cart = models.ForeignKey('user_auth.Cart')
    description = models.TextField()

    def __str__(self):
        return str(self.name + self.cart.user.username)
