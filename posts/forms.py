from .models import Advertise
from django import forms

class AdvertiseCreateForm(forms.ModelForm):
    class Meta:
        model = Advertise
        # fields = '__all__'
        fields = ('service_name','service_catg','service_img','service_disc','skill','price','charge_type')

