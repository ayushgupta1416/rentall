from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'shop/index.html')
def about(request):
    return render(request, 'shop/about.html')
def search(request):
    return render(request, 'shop/index.html')
def contact(request):
    return render(request, 'shop/index.html')
def productView(request):
    return render(request, 'shop/index.html')
def sellProduct(request):
    return render(request, 'shop/index2.html')
def signup(request):
    return render(request, 'shop/signup.html')



