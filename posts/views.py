from django.shortcuts import render
from .forms import AdvertiseCreateForm
from django.contrib.auth.decorators import login_required
# Create your views here.



@login_required
def  advertise_create(request):
    if request.method=="POST":
        form = AdvertiseCreateForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            new_advertise = form.save(commit=False)
            new_advertise.user = request.user
            new_advertise.save()
    
    else:
        form = AdvertiseCreateForm(data=request.POST)

    return render(request,'posts/create.html',{'form':form})

        
        
        