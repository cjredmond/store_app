from django.conf.urls import url, include
from django.conf.urls import url
from django.contrib import admin
from user_auth.views import UserCreateView, CartDetailView
from products.views import ProductListView, ProductDetailView, AddToCartView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include("django.contrib.auth.urls")),
    url(r'^create/user$', UserCreateView.as_view(), name="user_create_view"),
    url(r'^products/$', ProductListView.as_view(), name="product_list_view"),
    url(r'^product/(?P<pk>\d+)/$', ProductDetailView.as_view(), name='product_detail_view'),
    url(r'^product/(?P<pk>\d+)/add-to-cart/$', AddToCartView.as_view(), name='add_to_cart_view'),
    url(r'^cart/(?P<pk>\d+)/$', CartDetailView.as_view(), name='cart_detail_view'),
    

]
