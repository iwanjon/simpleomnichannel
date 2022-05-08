from ast import Or
from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Delivery)
admin.site.register(Order)
admin.site.register(Channel)
admin.site.register(Stock)
admin.site.register(Payment)