from django.shortcuts import render, get_object_or_404
from . models import Category, Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage


def allProducts(request, category_slug=None):
    categoryPage = None
    productList = None
    if category_slug != None:
        categoryPage = get_object_or_404(Category, slug=category_slug)
        productList = Product.objects.all().filter(category=categoryPage, productAvailable=True)
    else:
        productList = Product.objects.all().filter(productAvailable=True)
    paginator = Paginator(productList, 8)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)
    return render(request, 'allProduct.html', {'categoryObj': categoryPage, 'products': products})


def productDetails(request, category_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'productDetails.html', {'product': product})


