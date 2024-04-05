
"""farmo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name='about'),
    path("services", views.services, name='services'),
    path('<int:id>/', views.detail,name="detail"),
    path("contact/", views.contact_us, name='contact_us'),
    path("join-us/",views.join_us,name="join"),
    

    #services urls
    path("workers_page", views.worker_services, name="wokers"),
    path("machinorys_page", views.machinory_services, name="machinory"),
    # path("vehicals_page", views.vehical_services, name="vehicals")
    path("vehicals_page", views.testvehi, name="vehi")


    
]
