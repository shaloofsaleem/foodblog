from django.db import models
from django.template.defaultfilters import date, default

from shop.models import products

# Create your models here.
class cartlist(models.Model):
    cart_id=models.CharField(max_length=250,unique=True)
    date_added=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.cart_id



class item (models.Model):
    prodt=models.ForeignKey(products,on_delete=models.CASCADE)
    cart=models.ForeignKey(cartlist,on_delete=models.CASCADE)
    quan=models.IntegerField()
    active=models.BooleanField(default=True)


    def __str__(self):
        return self.prodt  



    def total(self):
        return self.prodt.price*self.quan         