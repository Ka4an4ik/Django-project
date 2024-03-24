from django.shortcuts import get_list_or_404, render 
from django.core.paginator import Paginator

from goods.models import Products, Categories

def catalog(request, category_slug, page = 1):

    categories = Categories.objects.all()


    if category_slug == 'all':
        goods = Products.objects.all()

    else:
        goods = get_list_or_404(Products.objects.filter(category__slug = category_slug))


    paginator = Paginator(goods, 3)
    current_page = paginator.page(page)

    goods = Products.objects.all()

    context = {
        "title": "Home - Каталог",
        "goods": current_page,
        "categories":categories,
        "slug_url": category_slug,
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):

    product = Products.objects.get(slug = product_slug)

    context = {
        'product' : product
    }
    


    return render(request, "goods/product.html", context)
