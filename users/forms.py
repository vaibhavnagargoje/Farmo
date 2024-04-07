from django import forms
from django.contrib.auth.models import User
from .models import Profile



class UserEditForm(forms.ModelForm):
    class Meta:
        model= User
        fields = ('first_name','last_name', 'email')
        # fields = '__all__'
        






class DateInput(forms.DateInput):  # for Dob Input dilog box 
    input_type = 'date'

class ProfileEditForm(forms.ModelForm):
    
    class Meta:
        model=Profile
        fields = '__all__'
        fields = ('photo','mobile','dob','gender','address','pincode','age','status')
        widgets = {
            'dob': DateInput()
        }
    
    def clean(self):
            cleaned_data= super().clean()
           
            # if((self.cleaned_data['pincode'])<=00000 and self.cleaned_data['pincode']>=999999):
            #     self.add_error("pincode","Enter Valid  Pin Code")                                 
        
            if(len(self.cleaned_data['mobile'])<10):
                # print(len(self.cleaned_data['mobile']))
                self.add_error("mobile","Please Enter 10 Digit Mobile Number")
                print("error occured")
            
            
            elif(self.cleaned_data['mobile'][0]) not in  ['7','9','8']:
                print("mobile start error")
                self.add_error("mobile"," Please Enter A Valid Mobile Number and Try Again  ")




class LoginForm(forms.Form):
    username= forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):

    password=forms.CharField(label='Password', widget=forms.PasswordInput())
    password2=forms.CharField(label='Confirm Password', widget=forms.PasswordInput())
    mobile = forms.CharField(label="mobile")



    class Meta:
        model=User
        fields =fields ={'username','email' , 'first_name','last_name','mobile'}

    # def check_password(self):
    #     cleaned_data = super(UserRegistrationForm, self).clean()
    #     if(self.cleaned_data['password']!=self.cleaned_data['password2']):
    #         raise forms.ValidationError("Password does not matched")
    #     return self.changed_data['password2']
    

    def clean(self):
        cleaned_data= super().clean()
        if(self.cleaned_data['password']!=self.cleaned_data['password2']):
            self.add_error("password2","Password does not matched...")
        
        if(len(self.cleaned_data['mobile'])<10):
            # print(len(self.cleaned_data['mobile']))
            self.add_error("mobile","Please Enter 10 Digit Mobile Number ")
        
        
        elif(self.cleaned_data['mobile'][0]) not in  ['7','9','8']:
            print("mobile start error")
            self.add_error("mobile"," Please Enter A Valid Mobile Number and Try Again  ")

            
        
        
     