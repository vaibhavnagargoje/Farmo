from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .models import  Profile
from .forms import UserEditForm, ProfileEditForm
from posts.forms import CommentForm
from django.contrib import messages
from posts.models import Advertise
from django.shortcuts import get_object_or_404
# Create your views here.


def user_login(request):
    if request.method =="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,username=data['username'],password=data['password'])
            if user is not None:
                login(request, user)
                current_user=request.user
                advertise = Advertise.objects.filter(user=current_user)
                profile =  Profile.objects.get(user=current_user)
                
                return redirect('home')

                # return render(request,'users',{'profile':profile})
                return render(request,'users',{'profile':profile})
                # return render(request,'users/index.html')
            else:
                messages.success(request,"Invalid Detail ! ")
                
                
                return redirect('login')


    else:

        form = LoginForm()
    return render(request,'users/login.html',{'form':form})


def user_logout(request):
    logout(request)
    return render(request,'users/logout.html')




@login_required
def index(request):
    if request.method =='POST':
        Inquiry_form = CommentForm(data=request.POST)
        new_inquiry = Inquiry_form.save(commit=False)
        post_id = request.POST.get('post_id')
        post=get_object_or_404(Advertise,id=post_id)
        new_inquiry.advertise = post
        new_inquiry.save()
    else:
        Inquiry_form=CommentForm()

    current_user=request.user
    advertise = Advertise.objects.filter(user=current_user)
    profile =  Profile.objects.get(user=current_user)
   

    return render(request,'users/index.html',{'current_user':current_user,'profile':profile,'advertises':advertise,'comment_form':Inquiry_form})





def register(request):
    if request.method=='POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user=user_form.save(commit=False)

           
        
            new_user.set_password(user_form.cleaned_data['password2'])
            new_user.save()
            Profile.objects.create(user=new_user)
            messages.success(request,"Registration Successful..")
            
            # return render(request,"index_4.html")
            return redirect('/users')






    else:
        user_form= UserRegistrationForm()
    return render(request,'users/register.html',{'user_form':user_form})



@login_required
def edit(request):
    if (request.method=="POST"):
        user_form =UserEditForm(instance=request.user,data=request.POST)
        profile_form= ProfileEditForm(instance=request.user.profile, data=request.POST,files=request.FILES)
        if (user_form.is_valid() and profile_form.is_valid()):
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
    
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        
    
    return render(request,'users/edit.html',{'user_form':user_form,'profile_form':profile_form})






@login_required
def edit_2(request):
    if request.method=='POST':
        user_form =UserEditForm(instance=request.user,data=request.POST)
        profile_form= ProfileEditForm(instance=request.user.profile, data=request.POST,files=request.FILES)
        print("edit successfull 1")
        if user_form.is_valid() and profile_form.is_valid():
            
            print("edit successfull 1-1")
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('/users')

    
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        print("edit successfull 2")
        
    
    print("edit successfull 3")
    return render(request,'users/edit.html',{'user_form':user_form,'profile_form':profile_form})


@login_required
def delete(request):
    user_form =UserEditForm(instance=request.user,data=request.POST)