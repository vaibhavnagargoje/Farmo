from django.db import models
# from datetime import datetime

# Create your models here.
# class contact(models.Model):
#     No = models.AutoField
#     Name = models.CharField(max_length=50)
#     email = models.CharField(max_length=50)
#     phone = models.CharField(max_length=200)
#     desc = models.CharField(max_length=200)
#     send_date = models.DateField()
#     # image= models.ImageField(upload_to="home/images")  
#     def __str__(self):
#         return self.Name
    

class seller_info(models.Model):
    class TypeChoices(models.TextChoices):
        WORKER= 'Worker'
        MACHINERY= 'Machinery'
        VEHICLES= 'Vehicles'
    class GenderChoies(models.TextChoices):
        MALE='Male'
        FEMALE='Female'
        OTHER ='Other'

    seller_name = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    dob = models.DateField()
    gender= models.CharField(max_length=10,choices=GenderChoies.choices)
    address= models.CharField(max_length=200)
    pincode= models.IntegerField()
    product_name= models.CharField(max_length=50)
    product_catg= models.CharField(max_length=10, choices=TypeChoices.choices)
    product_Disc= models.CharField(max_length=240)
    skill = models.CharField(max_length=50)
    price=models.IntegerField()
    seller_img=models.ImageField(upload_to="home/images")
    product_img= models.ImageField(upload_to="home/images", default="")
    register_date=models.DateField()
    status=models.BooleanField(default=False)
    age = models.IntegerField(default=18)

    def __str__(self):
        return self.seller_name 


class destiatiion:
    id :int
    name: str
    img: str
    desc :str
    price : int 


class Contact(models.Model):
    Name= models.CharField(max_length=100)
    Mail= models.CharField(max_length=100)
    Phone= models.CharField(max_length=15)
    Message= models.TextField()
    
    def __str__(self):
        return self.Name