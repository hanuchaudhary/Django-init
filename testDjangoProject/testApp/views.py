from django.shortcuts import render

# Create your views here.

def test_app(request):
    return render(request, 'testApp/testApp.html')