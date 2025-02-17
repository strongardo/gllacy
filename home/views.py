from django.shortcuts import render, redirect
from catalog.models import Product


def home_view(request):
    products = Product.objects.all()
    hits = products.filter(is_hit=True)
    # hits = Product.objects.filter(is_hit=True)
    return render(request, 'home.html', context={'hits': hits})