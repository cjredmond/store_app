from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy
from user_auth.models import Cart, Profile
from shipping.models import Shipment, OrderProduct
from products.models import CartProduct

class IndexView(TemplateView):
    template_name = "index.html"

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    def get_success_url(self):
        return reverse('login')

class CartDetailView(DetailView):
    model = Cart

class CartUpdateView(UpdateView):
    fields = []
    model = Cart
    success_url = '/'

    def form_valid(self, form, **kwargs):
        instance = form.save(commit=False)
        target = Cart.objects.get(id=self.kwargs['pk'])
        new = Shipment.objects.create(user=self.request.user)
        items = CartProduct.objects.filter(cart=target)
        for product in items:
            OrderProduct.objects.create(name=product.name, price=product.price, description=product.description, shipment=new, copy_product=Product.models.get(name=product.name))
        new.save()
        items.delete()
        return super().form_valid(form)

class ProfileDetailView(DetailView):
    model = Profile

class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ('address_num', 'address_street','address_city', 'address_state')

    def get_success_url(self):
        return reverse('profile_detail_view', args=str(self.request.user.profile.id))
    def form_valid(self,form):
        instance = form.save(commit=False)
        return super().form_valid(form)
