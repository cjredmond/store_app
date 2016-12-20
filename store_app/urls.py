from django.conf.urls import url, include
from django.conf.urls import url
from django.contrib import admin
from user_auth.views import UserCreateView, CartDetailView, CartUpdateView, ProfileDetailView, \
                            IndexView, ProfileUpdateView
from products.views import ProductListView, ProductDetailView, AddToCartView, RemoveFromCartView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include("django.contrib.auth.urls")),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^create/user$', UserCreateView.as_view(), name="user_create_view"),
    url(r'^products/$', ProductListView.as_view(), name="product_list_view"),
    url(r'^product/(?P<pk>\d+)/$', ProductDetailView.as_view(), name='product_detail_view'),
    url(r'^product/(?P<pk>\d+)/add-to-cart/$', AddToCartView.as_view(), name='add_to_cart_view'),
    url(r'^product/(?P<pk>\d+)/remove-from-cart/$', RemoveFromCartView.as_view(), name='remove_from_cart_view'),
    url(r'^cart/(?P<pk>\d+)/$', CartDetailView.as_view(), name='cart_detail_view'),
    url(r'^cart/(?P<pk>\d+)/checkout$', CartUpdateView.as_view(), name='cart_update_view'),
    url(r'^profile/(?P<pk>\d+)/$', ProfileDetailView.as_view(), name='profile_detail_view'),
    url(r'^profile/(?P<pk>\d+)/update/$', ProfileUpdateView.as_view(), name='profile_update_view'),
]
