from django.shortcuts import render
from django.views.generic import *
from .models import Gender, Product
from .forms import *
from django.contrib import messages


class ProductListView(ListView):
    template_name = 'store/index.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all()


class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/detail.html'
    context_object_name = 'details'


class SearchResultView(ListView):
    model = Product
    template_name = 'store/result.html'
    context_object_name = 'results'

    def get_queryset(self):
        query = self.request.GET['q']
        print(query)
        results = Product.objects.filter(name__icontains=query)
        return results





