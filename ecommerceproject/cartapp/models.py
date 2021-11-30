from django.db import models
from shopapp.models import product

#First we have to create tables Cart id,Date and time, products in the Carts

# Create your models here.
class Cart(models.Model):
    objects = None
    cart_id=models.CharField(max_length=250,blank=True)
    date_added=models.DateField(auto_now_add=True)

    #Using class meta
    class Meta:
        db_table='Cart'
        ordering=['date_added']

    #To show whic object to be shown in table
    def __str__(self):
        return '{}'.format(self.cart_id)


#Table to store the items in the cartapp
class CartItem(models.Model):
    objects = None
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)

    class Meta:
        db_table='CartItem'
    #subtotal  quantity X price

    def sub_total(self):
        return  self.product.price * self.quantity

    def __str__(self):
        return '{}'.format(self.product)
