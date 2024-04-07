from django.shortcuts import render
from .forms import AdvertiseCreateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.



@login_required
def  advertise_create(request):
    if request.method=="POST":
        form = AdvertiseCreateForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            new_advertise = form.save(commit=False)
            new_advertise.user = request.user
            new_advertise.save()
            messages.success(request, 'Your Services/Advertise Created or Successfully ')
    
    else:
        form = AdvertiseCreateForm(data=request.POST)

    return render(request,'posts/create.html',{'form':form})

        
        
        