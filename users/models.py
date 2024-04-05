from django.db import models
from django.conf import settings
# Create your models here.




class Profile(models.Model):
    class GenderChoies(models.TextChoices):
        MALE='Male'
        FEMALE='Female'
        OTHER ='Other'
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo= models.ImageField(upload_to='users/%Y/%M/%d',default='profile_user.jpg')
    mobile= models.CharField(max_length=15,blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    gender= models.CharField(max_length=10,choices=GenderChoies.choices,default=GenderChoies.MALE)
    address= models.CharField(max_length=200,blank=True, null=True)
    pincode= models.IntegerField(blank=True, null=True)
    age = models.IntegerField(default=18)
    register_date=models.DateField(auto_now_add=True)




    def __str__(self):
        return self.user.username


# class Inquiry(models.Model):
#     adverti