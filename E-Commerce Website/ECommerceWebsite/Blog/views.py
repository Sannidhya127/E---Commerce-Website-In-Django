from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def BlogHome(request):
    return render(request, 'Blog/index.html')
