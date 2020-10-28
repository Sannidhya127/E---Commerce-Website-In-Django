from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'shop/index.html')


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return HttpResponse("Contact Us")


def track(request):
    return HttpResponse("Track Order")


def search(request):
    return HttpResponse("Search Order")


def productview(request):
    return HttpResponse("View Product")


def checkout(request):
    return HttpResponse("Checkout")
