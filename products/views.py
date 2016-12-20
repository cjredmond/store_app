from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from products.models import Product, CartProduct

class ProductListView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product

class AddToCartView(CreateView):
    model = CartProduct
    fields = []
    success_url = "/"

    def form_valid(self, form, **kwargs):
        instance = form.save(commit=False)
        target = Product.objects.get(id=self.kwargs['pk'])
        instance.cart = self.request.user.cart
        instance.name = target.name
        instance.price = target.price
        instance.description = target.description
        target.stock = target.stock - 1
        target.save()
        return super().form_valid(form)
