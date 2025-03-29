from django.db import models
from django.contrib.auth.models import User
from store.models import Product
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from datetime import datetime

class ShippingAddress(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    shippingfull_name=models.CharField(max_length=200)
    shipping_EmailAddress=models.CharField(max_length=200)
    shipping_phonenumber=models.CharField(max_length=200)
    shipping_country=models.CharField(max_length=200)
    shipping_state=models.CharField(max_length=200)
    shipping_district=models.CharField(max_length=200)
    shipping_city=models.CharField(max_length=200)
    shipping_zipCode=models.CharField(max_length=200)
   
    class Meta:
        verbose_name_plural="Shipping Address"
    def __str__(self):
        return f'Shipping Address - {str(self.id)}'   
 
# create user profile default when user signup

def create_shipping(sender,instance,created, **kwargs):
    if created:
        user_shipping=ShippingAddress(user=instance)
        user_shipping.save()
post_save.connect(create_shipping,sender=User)        
    
      # order model 
class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    full_name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    phone_number=models.CharField(max_length=15,blank=True)
    shipping_address=models.TextField(max_length=500)
    amount_paid=models.DecimalField(max_digits=10,decimal_places=2)
    date_ordered=models.DateTimeField(auto_now_add=True)
    shipped=models.BooleanField(default=False)
    date_shipped=models.DateTimeField(blank=True,null=True)
    def __str__(self):
        return f'Order - {str(self.id)}'
    # add auto date shipped
@receiver(pre_save,sender=Order)
def set_date_shipped(sender,instance,**kwargs):
    if instance.pk:
        now = datetime.now()
        obj=sender._default_manager.get(pk=instance.pk)
        if instance.shipped and not obj.shipped:
            instance.date_shipped=now
            
class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)  
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    quantity=models.PositiveBigIntegerField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return f'Order item - {str(self.id)}'
    
    
     
    

