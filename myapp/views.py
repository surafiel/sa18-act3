from django.shortcuts import render
from .models import Product

def index(request):
    products = Product.objects.all()
    return render(request, 'myapp/index.html', {'products': products})

def show(request, id):
    product = Product.objects.get(pk=id)
    return render(request, 'myapp/show.html', {'product': product})