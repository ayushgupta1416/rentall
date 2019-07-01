from django.shortcuts import render


def login(request):
    return render(request, 'shop/index1.html')
