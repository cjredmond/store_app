from django.contrib import admin

from products.models import Product, CartProduct
admin.site.register(Product)
admin.site.register(CartProduct)
