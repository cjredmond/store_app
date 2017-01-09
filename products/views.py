from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from products.models import Product, CartProduct, Review
from shipping.models import OrderProduct
from django.urls import reverse, reverse_lazy

class ProductListView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product

class AddToCartView(CreateView):
    model = CartProduct
    fields = []
    def get_success_url(self, **kwargs):
        return reverse('product_list_view')

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

class RemoveFromCartView(DeleteView):
    model = CartProduct

    def get_success_url(self, **kwargs):
        current = CartProduct.objects.get(id=self.kwargs['pk'])
        target = Product.objects.get(name=current.name)
        target.stock += 1
        target.save()
        return reverse('profile_detail_view', args=str(self.request.user.profile.id))

class ReviewCreateView(CreateView):
    model = Review
    fields = ('text', 'rating')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.get(id=self.kwargs['pk'])
        return context

    def get_success_url(self, **kwargs):
        return reverse('product_list_view')

    def form_valid(self, form, **kwargs):
        instance = form.save(commit=False)
        target = Product.objects.get(id=self.kwargs['pk'])
        #new_target = Product.objects.get(name=target.name)
        instance.product = target
        instance.user = self.request.user
        return super().form_valid(form)
