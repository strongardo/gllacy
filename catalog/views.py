from django.shortcuts import render
from .models import Product
from .forms import FilterForm


def catalog(request):
    products = Product.objects.all()
    form = FilterForm(request.GET)
    if form.is_valid():
        if form.cleaned_data['fat']:
            fat_value = form.cleaned_data['fat']
            if fat_value == 'zero':
                products = products.filter(fat=0)
            elif fat_value == 'up_to_ten':
                products = products.filter(fat__lte=10)
            elif fat_value == 'up_to_thirty':
                products = products.filter(fat__lt=30)
            elif fat_value == 'above_thirty':
                products = products.filter(fat__gte=30)
        if form.cleaned_data['fillers']:
            selected_fillers = form.cleaned_data['fillers']
            products = products.filter(fillers__name__in=selected_fillers).distinct()
        if form.cleaned_data['min_price']:
            min_price = form.cleaned_data['min_price']
            products = products.filter(price__gte=min_price)
        if form.cleaned_data['max_price']:
            max_price = form.cleaned_data['max_price']
            products = products.filter(price__lte=max_price)

    return render(request, 'catalog.html', context={'products': products})
