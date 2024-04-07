from .models import Advertise,Inquiry,Reports
from django import forms

class AdvertiseCreateForm(forms.ModelForm):
    class Meta:
        model = Advertise
        # fields = '__all__'
        fields = ('service_name','service_catg','service_img','service_disc','skill','price','charge_type','status')




class DateInput(forms.DateInput):  # for Dob Input dilog box 
    input_type = 'date'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ('message','posted_by','work_date','inquiry_mobile')
        widgets = {
            'work_date': DateInput()
        }


    

class ReportsAdvertise(forms.ModelForm):
    class Meta:
        model = Reports
        fields = ('message','posted_by')