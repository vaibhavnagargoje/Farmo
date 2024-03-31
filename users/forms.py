from django import forms
from django.contrib.auth.models import User
from .models import Profile



class UserEditForm(forms.ModelForm):
    class Meta:
        model= User
        fields = ('first_name','last_name', 'email')






class DateInput(forms.DateInput):  # for Dob Input dilog box 
    input_type = 'date'

class ProfileEditForm(forms.ModelForm):
    
    class Meta:
        model=Profile
        fields = '__all__'
        widgets = {
            'dob': DateInput()
        }




class LoginForm(forms.Form):
    username= forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):

    password=forms.CharField(label='Password', widget=forms.PasswordInput())
    password2=forms.CharField(label='Confirm Password', widget=forms.PasswordInput())



    class Meta:
        model=User
        fields =fields ={'username','email' , 'first_name','last_name'}

    def check_password(self):
        cleaned_data = super(UserRegistrationForm, self).clean()
        if(self.cleaned_data['password']!=self.cleaned_data['password2']):
            raise forms.ValidationError("Password does not match")
        return self.changed_data['password2']
    

