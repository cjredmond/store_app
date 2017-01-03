from django.contrib import admin

from products.models import Product, CartProduct, Review
admin.site.register(Product)
admin.site.register(CartProduct)
admin.site.register(Review)
