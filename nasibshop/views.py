from django.shortcuts import render


def home(request):
    return render(request , 'home.html' )



def kharid(request):
    return render(request , 'kharid.html')
