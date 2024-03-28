from django.urls import path
from . import  views
from django.contrib.auth import views as auth_view
urlpatterns = [
    
    path('login/',views.user_login,name='login'),
    # path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html')),
    path('logout/',views.user_logout,name="logout"),


] 