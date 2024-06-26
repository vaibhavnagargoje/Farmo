from django.db import models
from django.conf import settings
from django.utils.text import slugify

# Create your models here.

class Advertise(models.Model):

    class TypeChoices(models.TextChoices):
        WORKER= 'Workers'
        MACHINERY= 'Machinerys'
        VEHICLES= 'Vehicles'
    class ChargeType(models.TextChoices):
        HR='Hour'
        DAY="Day"
        KM= "Km"

    user =models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    slug = models.SlugField(max_length=500,blank=True)
    
    service_name = models.CharField(max_length=50)
    service_catg= models.CharField(max_length=10, choices=TypeChoices.choices)
    service_disc= models.CharField(max_length=240)
    skill = models.CharField(max_length=50)
    price=models.IntegerField()
    charge_type=models.CharField(max_length=10,choices=ChargeType.choices,default='Day' )
    
    service_img= models.ImageField(upload_to="home/images", default="")
    register_date=models.DateField(auto_now_add=True)
    status=models.BooleanField(default=False,)

    


    def __str__(self):
        return self.user.username
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.service_name)

        super().save(*args,**kwargs)




class Inquiry(models.Model):
    advertise = models.ForeignKey(Advertise, on_delete=models.CASCADE,related_name='inquirys')
    message=models.CharField(max_length=100)
    inquiry_mobile=models.BigIntegerField()
    created=models.DateTimeField(auto_now=True)
    work_date=models.DateField(blank=True, null=True)

    posted_by= models.CharField(max_length=100)

    class Meta:
        ordering=('created',)

    def __str__(self):
        return self.message
    


class Reports(models.Model):
    advertise= models.ForeignKey(Advertise,on_delete=models.CASCADE, related_name='reports')
    message=models.CharField(max_length=300)
    created =models.DateTimeField(auto_now=True)
    posted_by= models.CharField(max_length=100)
    # document= models.ImageField(upload_to="home/images", default="")


    class Meta:
        ordering=('created',)

    def __str__(self):
        return self.message

    