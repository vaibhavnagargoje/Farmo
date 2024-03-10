from django import forms
from .models import Contact , seller_info

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields=['Name','Mail','Phone', 'Message']


class SellerForm(forms.ModelForm):
    class Meta:
        model = seller_info
   
    
        fields = ['seller_name','mobile','gender','address','pincode','product_name','product_catg','product_Disc','price','seller_img','product_img','status','skill']