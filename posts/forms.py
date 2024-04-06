from .models import Advertise,Inquiry
from django import forms

class AdvertiseCreateForm(forms.ModelForm):
    class Meta:
        model = Advertise
        # fields = '__all__'
        fields = ('service_name','service_catg','service_img','service_disc','skill','price','charge_type','status')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ('message','posted_by')