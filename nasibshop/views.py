from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from product.models import Product , Cart


def home(request):
    context = {}
    products = Product.objects.all()

    context['products'] = products

    return render(request , 'home.html' , context )




@login_required(login_url = "/accounts/login")
def kharid(request):
    return render(request , 'kharid.html')
