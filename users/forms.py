from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username= forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):

    password=forms.CharField(label='Password')
    password2=forms.CharField(label='Confirm Password', widget=forms.PasswordInput)



    class Meta:
        model=User
        fields ={'username','email' , 'first_name','last_name'}

    def check_password(self):
        if(self.changed_data['password']!=self.changed_data['password2']):
            raise forms.ValidationError("Password  does not match")
        return self.changed_data['password2']