# from dataclasses import field
# from pyexpat import model
from django import forms

from .models import Customer, Product, Stock, Channel,Payment,Order,Delivery

class CustomerForm(forms.ModelForm):
    class Meta:
        model= Customer
        # exclude=["post"]
        # exclude = ('email',)
        fields= "__all__"
        # labels = {
        #     "username":"your name",
        #     "email":"your email",
        #     "text":"your comment"
        # }
        
        
class ProductForm(forms.ModelForm):
    class Meta:
        model= Product
        fields= ['channel', 'code', 'id', 'name', 'status'] 
        
        
class DeliveryForm(forms.ModelForm):
    class Meta:
        model= Delivery
        fields= "__all__"
        
class StockForm(forms.ModelForm):
    class Meta:
        model= Stock
        fields= "__all__"
        
class ChannelForm(forms.ModelForm):
    class Meta:
        model= Channel
        fields= "__all__"
        
class OrderForm(forms.ModelForm):
    class Meta:
        model= Order
        fields= "__all__"
        
class PaymentForm(forms.ModelForm):
    class Meta:
        model= Payment
        fields= "__all__"
