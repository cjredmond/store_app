from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    adress_num = models.IntegerField(blank=True,null=True)
    adress_street = models.CharField(max_length=40,blank=True,null=True)
    adress_city = models.CharField(max_length=40,blank=True,null=True)
    adress_state = models.CharField(max_length=2,blank=True,null=True)

    def __str__(self):
        return str(self.user.username)

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
        return sum([product.price for product in self.items])
