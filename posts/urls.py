from django.urls import path
from . import  views
urlpatterns = [
    
    path('create/',views.advertise_create,name='create'),

   
    
    ] 