from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    address_num = models.IntegerField(blank=True,null=True)
    address_street = models.CharField(max_length=40,blank=True,null=True)
    address_city = models.CharField(max_length=40,blank=True,null=True)
    address_state = models.CharField(max_length=2,blank=True,null=True)

    def __str__(self):
        return str(self.user.username)

    @property
    def shipments(self):
        return self.user.shipment_set.all()

@receiver(post_save, sender=User)
def create(**kwargs):
    created = kwargs['created']
    instance = kwargs['instance']
    if created:
        Profile.objects.create(user=instance)
        Cart.objects.create(user=instance)

class Cart(models.Model):
    user = models.OneToOneField('auth.User')

    def __str__(self):
        return str(self.user.username)

    @property
    def items(self):
        return self.cartproduct_set.all()

    def total(self):
        return round(sum([product.price for product in self.items]),2)
