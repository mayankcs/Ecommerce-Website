from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class customer(models.Model):
    customer_username=models.OneToOneField(User,on_delete=models.CASCADE, related_name='customername',null=False)
    phone_number=models.IntegerField()
    def __str__(self):
        return '%s' % (self.customer_username.username)

class seller(models.Model):
    seller_username=models.OneToOneField(User,on_delete=models.CASCADE, related_name='sellername',null=False)
    shop_name=models.CharField(max_length=20,default=None)
    phone_number=models.IntegerField()
    address=models.CharField(max_length=50)
    apartment=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    pincode=models.IntegerField()
    total_earning=models.IntegerField(default=0)
    
    def __str__(self):
        return '%s' % (self.seller_username.username)
   

