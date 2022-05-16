
from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from app.models import *
 


class ChannelSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Channel
        fields= '__all__'
        

class ProductSerializers(serializers.ModelSerializer):
    channel=ChannelSerializers(read_only=True)
    
    class Meta:
        model = Product
        fields= '__all__'


class StockSerializers(serializers.ModelSerializer):
    product= ProductSerializers(read_only=True)
    
    class Meta:
        model = Stock
        fields= '__all__'


class DeliverySerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Delivery
        fields= '__all__'


class PaymentSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Payment
        fields= '__all__'
        
        
class OrderSerializers(serializers.ModelSerializer):
    product= ProductSerializers(many=True, read_only=True)
    # payment= PaymentSerializers()
    # delivery= DeliverySerializers()

# reference   
#   https://stackoverflow.com/questions/60880463/django-rest-framework-nested-serializer-create-method
#  post data when use nested serializer, so "get" method keeo show dict of nested data,
# but "post"  method can be done just by using id of nested serilizer data
########  option number 1
########  option number 1
    def to_internal_value(self, data):
        print("dddd", data,"ffff", self)
        classes_pk = data.get('product')
        ret = super().to_internal_value(data)
        print(ret,"dddd", data,"ffff", self)
        try:
            queryset = Product.objects.none()
            for i in classes_pk:
                queryset |= Product.objects.filter(pk=i)
        except Product.DoesNotExist:
            raise ValidationError(
                {'classes': ['Invalid classes primary key']},
                code='invalid',
            )
        ret['product'] = queryset
        return ret   
    ######## end of  option number 1 
    ######## end of  option number 1 
    
    class Meta:
        model = Order
        fields= '__all__'
    ########  option number 2
    ########  option number 1
    #     fields= ('invoice',
    #             'is_paid',
    #             'destination',
    #             'product',
    #             'payment',
    #             'delivery',
    #             'product_id',)
    #     extra_kwargs = {
    #   'product_id': {'source': 'product', 'write_only': True},
    #             }
    ####### end of  option number 2 
    ####### end of  option number 2   
        
class CustomerSerializers(serializers.ModelSerializer):
    # order=OrderSerializers(read_only=True)
    
    class Meta:
        model = Customer
        fields= '__all__'
