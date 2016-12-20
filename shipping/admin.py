from django.contrib import admin

from shipping.models import Shipment, OrderProduct
admin.site.register(Shipment)
admin.site.register(OrderProduct)
