from django.db import models
from product.models import product
from account.models import customer, seller
# Create your models here.

class cart(models.Model):
    user_id=models.ForeignKey(customer,on_delete=models.CASCADE, related_name='customer_id',null=False)
    seller_id=models.ForeignKey(seller,on_delete=models.CASCADE, related_name='seller_id',null=False)
    product_id=models.ForeignKey(product,on_delete=models.CASCADE, related_name='product_id',null=False)
    def __str__(self):
        return '%s added %s to cart' % (self.user_id ,self.product_id)

class purchased(models.Model):
    user_id=models.ForeignKey(customer,on_delete=models.CASCADE, related_name='pcustomer_id',null=False)
    seller_id=models.ForeignKey(seller,on_delete=models.CASCADE, related_name='pseller_id',null=False)
    product_id=models.ForeignKey(product,on_delete=models.CASCADE, related_name='pproduct_id',null=False)
    def __str__(self):
        return '%s purchased %s' % (self.user_id ,self.product_id)