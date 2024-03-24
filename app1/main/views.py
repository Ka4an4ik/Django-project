from django.shortcuts import render
from django.http import HttpResponse

from goods.models import Categories


def index(request):


    categories = Categories.objects.all()

    context = {

        "categories" : categories,
    }

    return render(request, 'main/index.html', context)


def about(request):

    return render(request, 'main/about.html')

