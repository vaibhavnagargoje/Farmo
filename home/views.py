from django.shortcuts import render
from .models import seller_info
from math import ceil
from django.http import HttpResponse 
from .models import destiatiion
# Create your views here.
def index(request):
    # seller_data = seller_info.objects.all()
    # n=len(seller_data)
    # print(n)
    # print(seller_data)
    # nSlides= n//4 + ceil((n/4)+(n//4))
    # print(nSlides)

    # parameter = { "total_slides":nSlides,'range':range(1,nSlides),'data':seller_data}

    # all_data= [[seller_data, range(1,nSlides),nSlides],
    #             [ seller_data, range(1,nSlides),nSlides]
    #         ]

    all_data=[]
    prod_catgs=seller_info.objects.values("product_catg")
    catg={item['product_catg'] for item in prod_catgs}
    for cat in catg:
        product=seller_info.objects.filter(product_catg=cat)
        n=len(product)
        nSlides= n//4 + ceil((n/4)+(n//4))


        all_data.append([product, range(1,nSlides), nSlides])




    parameter={'all_data':all_data}
    return render( request,"index.html", parameter)

def about(request):
    return render(request,"about.html")

def contact_us(request):
    return render(request,"contact_us.html")

    
def services(request):
    return render(request,"services.html")

def worker_services(request):
    dest_all = seller_info.objects.all()
    return render(request,"workers_page.html",{'dests': dest_all})


def index(request):
    # seller_data = seller_info.objects.all()
    # n=len(seller_data)
    # print(n)
    # print(seller_data)
    # nSlides= n//4 + ceil((n/4)+(n//4))
    # print(nSlides)

    # parameter = { "total_slides":nSlides,'range':range(1,nSlides),'data':seller_data}

    # all_data= [[seller_data, range(1,nSlides),nSlides],
    #             [ seller_data, range(1,nSlides),nSlides]
    #         ]

    all_data=[]
    prod_catgs=seller_info.objects.values("product_catg")
    catg={item['product_catg'] for item in prod_catgs}
    for cat in catg:
        product=seller_info.objects.filter(product_catg=cat)
        n=len(product)
        nSlides= n//4 + ceil((n/4)+(n//4))


        all_data.append([product, range(1,nSlides), nSlides])




    parameter={'all_data':all_data}
    return render( request,"index_2.html", parameter)

def about(request):
    return render(request,"about.html")

def contact_us(request):
    return render(request,"contact_us.html")

    
def services(request):
    return render(request,"services.html")

def worker_services(request):
    dest_all = seller_info.objects.all()
    return render(request,"workers_page.html",{'dests': dest_all})




    

def machinory_services(request):
    dest_all = seller_info.objects.all()
    return render(request,"machinory.html",{'dests': dest_all})

    # return render(request,"machinory.html")

def vehical_services(request):

    dest_all = seller_info.objects.all()
    return render(request,"vehicals.html",{'dests': dest_all})




    
    
    