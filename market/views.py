from django.shortcuts import render
from .models import Product, Specification



def index(request):
    print('hi')
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'market/index.html', context)

def product(request, product_id):
    product_spec = Specification.objects.get(pk=product_id)
    context = {'product_spec': product_spec}
    return render(request, 'market/product.html', context)