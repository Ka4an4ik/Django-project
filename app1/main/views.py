from django.shortcuts import render
from django.http import HttpResponse

def second(request):
    return render(request, 'main/second.html')



