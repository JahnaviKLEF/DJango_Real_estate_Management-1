from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    data_created = models.DateTimeField(auto_now_add=True, null=True)
    
    
    def __str__(self):
        return self.user.username
    
    def create_Profile(sender, **kwargs):
        if kwargs['created']:
            user_profile = Customer.objects.create(user=kwargs['instance'])

class Sell(models.Model):
    property_name = models.CharField(max_length=100,default="")
    image = models.ImageField(upload_to='img/%y',default="")
    
    def __str__(self):
        return self.property_name
    



        

    
    
