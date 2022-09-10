from django.shortcuts import render, HttpResponse
from .models import seller_info
from math import ceil

# Create your views here.
def index(request):

    # seller_data = seller_info.objects.all()
    # print(seller_data)
    # n=len(seller_data)
    # total_slide = n//4 + ceil((n/4)-(n//4))

    # data_parameters = {'total_slide' : total_slide, 'range':range(1,total_slide), 'seller_data': seller_data}

    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact_us(request):
    return render(request,"contact_us.html")

    
def services(request):
    return render(request,"services.html")
    
    
    