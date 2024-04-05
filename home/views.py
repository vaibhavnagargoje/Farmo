from django.shortcuts import render,redirect
from .models import seller_info
from users.models import Profile
from posts.models import Advertise
from math import ceil
from django.http import HttpResponse 
from .models import destiatiion
from django.db.models import Q
from .forms import ContactForm
from django.contrib import  messages

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
    return render( request,"index_4.html", parameter)

def about(request):
    return render(request,"about.html")









def services(request):
    return render(request,"services.html")

def worker_services(request):
    dest_all = seller_info.objects.all()
    return render(request,"workers_page.html",{'dests': dest_all})


def index(request):

    all_data=[]
    prod_catgs=seller_info.objects.values("product_catg")

    # 
    search_name= request.GET.get('search_name')
    if search_name!='' and search_name is not None:
        prod_catgs = prod_catgs.filter(Q(product_name__icontains=search_name)| Q(product_catg__icontains=search_name)|Q(seller_name__icontains=search_name)|Q(address__icontains=search_name))
    
    else:
        pass
    catg={item['product_catg'] for item in prod_catgs}  

    # 
    for cat in catg:
        product=seller_info.objects.filter(product_catg=cat)
        n=len(product)
        nSlides= n//4 + ceil((n/4)+(n//4))


        all_data.append([product, range(1,nSlides), nSlides])

    parameter={'all_data':all_data}
    return render( request,"index_4.html", parameter)

    # serch logic 
        
    dest_all = seller_info.objects.all()
    search_name= request.GET.get('search_name')
    if search_name!='' and search_name is not None:
        dest_all = dest_all.filter(Q(product_name__icontains=search_name)| Q(product_catg__icontains="Machinery")|Q(seller_name__icontains=search_name)|Q(address__icontains=search_name))
        
    else:
        pass
    return render(request,"machinory.html",{'dests': dest_all})









def about(request):
    return render(request,"about.html")



    
def services(request):
    return render(request,"services.html")

def worker_services(request):

    # #old seller workr page logic 
    # dest_all = seller_info.objects.all()
    # search_name= request.GET.get('search_name')
    
    # if search_name!='' and search_name is not None:
    #     dest_all = dest_all.filter(Q(product_name__icontains=search_name)| Q(product_catg__icontains=search_name)|Q(seller_name__icontains=search_name)|Q(address__icontains=search_name))
    
    # else:
    #     pass
    # return render(request,"workers_page.html",{'dests': dest_all})


    dest_all = Advertise.objects.all()


    search_name= request.GET.get('search_name')
    
    if search_name!='' and search_name is not None:
       dest_all = dest_all.filter(Q(service_catg__icontains="worker")|Q(service_catg__icontains=search_name)|Q(service_name__icontains=search_name)|Q(skill__icontains=search_name))
        
    else:
        pass
    


    return render(request,"workers_page.html",{'dests': dest_all})
    
    return render(request,'testvehi.html',{'dests':dest_all})



    

def machinory_services(request):

    # ## old logic for seller table 
    # dest_all = seller_info.objects.all()
    # search_name= request.GET.get('search_name')
    
    # if search_name!='' and search_name is not None:
    #    dest_all = dest_all.filter(Q(product_name__icontains=search_name)| Q(product_catg__icontains="machinory")|Q(seller_name__icontains=search_name)|Q(address__icontains=search_name))
        
    # else:
    #     pass
    # return render(request,"machinory.html",{'dests': dest_all})


    dest_all = Advertise.objects.all()


    search_name= request.GET.get('search_name')
    
    if search_name!='' and search_name is not None:
       dest_all = dest_all.filter(Q(service_catg__icontains="machinory")|Q(service_catg__icontains=search_name)|Q(service_name__icontains=search_name)|Q(skill__icontains=search_name))
        
    else:
        pass
    


    
    return render(request,"machinory.html",{'dests': dest_all})

    # return render(request,"machinory.html")


#old seller info table 
def vehical_services(request):
    dest_all = seller_info.objects.all()
    search_name= request.GET.get('search_name')
    
    if search_name!='' and search_name is not None:
       dest_all = dest_all.filter(Q(product_name__icontains=search_name)| Q(product_catg__icontains="Vehical")|Q(seller_name__icontains=search_name)|Q(address__icontains=search_name))
        
    else:
        pass
    return render(request,"vehicals.html",{'dests': dest_all})




  



def detail(request,id):
    ## seler info tabel data 
    # dest_all= seller_info.objects.get(id=id)
    # return render(request,"detail.html",{'dest':dest_all})

    # Advertise tabel data 
    dests = Advertise.objects.get(id=id)
    print(dests)
    return render(request,'detail.html',{'dest':dests})

    


    
    

def contact_us(request):
    
    form =ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,"Your message has been sent.")
        return redirect('/')        

    return render(request,"contact.html",{'form':form})


def join_us(request):
    # form = SellerForm(request.POST or None)
    # if form.is_valid():
    #     form.save()
    #     return redirect('/')
    return render(request,"join-us.html")







def testvehi(request):
    
    dest_all = Advertise.objects.all()


    search_name= request.GET.get('search_name')
    
    if search_name!='' and search_name is not None:
       dest_all = dest_all.filter(Q(service_catg__icontains="Vehical")|Q(service_catg__icontains=search_name)|Q(service_name__icontains=search_name)|Q(skill__icontains=search_name))
        
    else:
        pass
    


    
    return render(request,'testvehi.html',{'dests':dest_all})