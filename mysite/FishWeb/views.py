from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from .models import Item


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')

class ProductView(View):
    def get(self, request):
        return render(request, 'products.html')

class StoreView(View):
    def get(self, request):
        return render(request, 'store.html')

class FishView(ListView):
    model = Item
    template_name = 'product.html'
