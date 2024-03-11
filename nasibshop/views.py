from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request , 'home.html' )


@login_required(login_url = "/accounts/login")
def kharid(request):
    return render(request , 'kharid.html')
