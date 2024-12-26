from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Welcome to the Django Project!")
    return render(request, 'homepage/index.html')


def about(request):
    # return HttpResponse("About us")
    return render(request, 'aboutpage/index.html')

def contact(request):
    # return HttpResponse("Contact us")
    return render(request, 'contactpage/index.html')


def json(request):
    # return JsonResponse({"name": "John", "age": 30})
    return render(request,"jsonpage/index.html")