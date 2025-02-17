from django.shortcuts import render, redirect
from .forms import NewsletterForm, FeedbackForm, SearchForm
from catalog.models import Product


def ty(request):
    return render(request, 'ty.html')


def newsletter(request):
    if request.method == 'POST':
        # print(request.POST['email'])

        form = NewsletterForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['email'])
            return redirect('ty')
        else:
            # print(form.errors) В HTML-формате
            # return render(request, 'home.html', context={'newsletter_form': form})
            print(form.errors.as_text())

    return redirect('home_url')


def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['message'])
            return redirect('ty')
        else:
            print(form.errors.as_text())

    return redirect('home_url')


def search(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            products = Product.objects.filter(name__icontains=form.cleaned_data['search_value'])
            return render(request, 'search.html', {'products': products})

    return render(request, 'search.html')
