from django.db import models
from account.models import seller ,customer
# Create your models here.

class category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return '%s' % (self.name)

class product(models.Model):
    seller=models.ForeignKey(seller,on_delete=models.CASCADE, related_name='product_name',null=False)
    name=models.CharField(max_length=100)
    category=models.ForeignKey(category,on_delete=models.CASCADE,related_name='product_category',null=False)
    image=models.ImageField(upload_to='Product_images')
    imformation=models.CharField(max_length=400)
    quantity=models.IntegerField()
    price=models.IntegerField()
    def __str__(self):
        return '%s' % (self.name)



class productFeedback(models.Model):
    feedback_by=models.ForeignKey(customer,on_delete=models.CASCADE, related_name='customer_name',null=False)
    product=models.ForeignKey(product,on_delete=models.CASCADE,related_name='product_name',null=False)
    feedback=models.CharField(max_length=200)
    def __str__(self):
        return '%s' % (self.feedback)



    