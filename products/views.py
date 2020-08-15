from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from products.models import Product


class ProductListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.all().order_by('timestamp')
        context['products'] = products
        return context

class ProductDetailView(DetailView):
    model = Product
    