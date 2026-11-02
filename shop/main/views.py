from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    # return HttpResponse("Hello World")
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')