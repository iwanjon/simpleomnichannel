from asyncio.windows_events import NULL
from itertools import product
from django.db import models
from django.forms import NullBooleanField

# Create your models here.
# Design Django model untuk omni channel order management:
# - Customer
# - Product
# - Stock
# - Payment
# - Order
# - Delivery
# - Channel

# Create simple product management in Django:
# - Product List View
# - Product Form View
# - Product Detail View
# - Product Upload View

# Notes:
# - Uplaod product support async process with progress bar
# - Use Django generic view and form

class Customer(models.Model):
    first_name= models.CharField(max_length=30)
    last_name= models.CharField(max_length=30)
    email= models.EmailField()
    image= models.ImageField(blank =True, null=True)
    handphone= models.IntegerField()
    address= models.CharField(max_length=100)
    order=models.OneToOneField("Order",  on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.first_name
    
    
class Product(models.Model):
    name= models.CharField(max_length=50)
    code= models.CharField(max_length=10)
    channel=models.OneToOneField("Channel",  on_delete=models.CASCADE, null=True)
    status=models.BooleanField(null=True)
    
    def __str__(self):
        return self.name
    
    
class Stock(models.Model):
    stock=models.IntegerField()
    product = models.OneToOneField("Product",  on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.stock
    
    
class Payment(models.Model):
    bank=models.CharField(max_length=20)
    created=models.DateTimeField(auto_now=True)
    status=models.BooleanField(null=True)
    
    def __str__(self):
        return self.bank
    
    
class Order(models.Model):
    invoice=models.CharField(max_length=30)
    created=models.DateTimeField(auto_now=True)
    is_paid=models.BooleanField(default=False)
    destination=models.CharField(max_length=100)
    product = models.ManyToManyField("Product")
    payment=models.ForeignKey("Payment", on_delete=models.CASCADE, null=True)
    delivery=models.ForeignKey("Delivery", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.invoice
    
    
class Delivery(models.Model):
    service= models.CharField(max_length=50)
    provider= models.CharField(max_length=50, blank=True, null=True)
    status=models.BooleanField(null=True)

    def __str__(self):
        return self.provider
    
    
class Channel(models.Model):
    name= models.CharField(max_length=50)
    status=models.BooleanField(null=True)
    
    def __str__(self):
        return self.name