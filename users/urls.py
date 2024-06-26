from django.urls import path
from . import  views
from django.contrib.auth import views as auth_view
urlpatterns = [
    
    path('',views.index,name='index'),
    path('login/',views.user_login, name='login'),
    path('logout/',views.user_logout,name="logout"),             # path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html')),

    path("password_change/",auth_view.PasswordChangeView.as_view(template_name='users/password_change_form.html'),name='password_change'),
    path("password_change/done/",auth_view.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),name="password_change_done"),
    path('password_reset/' ,auth_view.PasswordResetView.as_view(template_name = 'users/password_reset_form.html'),name= 'password_reset' ), 
    
    
    path('register/',views.register,name='register'),
    path('edit/',views.edit_2,name='edit'),

    path('delete_inquiry/<int:inquiry_id>/', views.delete_inquiry, name='delete_inquiry'),
    
    ] 