from cgitb import lookup
import django_filters
from .models import *

class ChannelFilter(django_filters.FilterSet):
    STAT_CHOICES        = (
                            (0, 'non active'),
                            (1, 'active')
    )
    name = django_filters.CharFilter(field_name="name",lookup_expr='icontains',label="name")
    status = django_filters.ChoiceFilter(field_name="status",
                                       lookup_expr='iexact', 
                                       label="status",
                                       choices   =STAT_CHOICES)

    class Meta:
        model = Channel
        fields = '__all__'
        


class ProductFilter(django_filters.FilterSet):
    STAT_CHOICES        = (
                            (0, 'non active'),
                            (1, 'active')
    )
    name = django_filters.CharFilter(field_name="name",lookup_expr='icontains',label="name")
    status = django_filters.BooleanFilter(field_name="status",
                                       label="status")
    # status = django_filters.ChoiceFilter(field_name="status",
    #                                    lookup_expr='iexact', 
    #                                    label="status",
    #                                    choices   =STAT_CHOICES)
    channel=django_filters.ModelChoiceFilter(queryset=Channel.objects.all())
    
    class Meta:
        model = Product
        fields = '__all__'


class StockFilter(django_filters.FilterSet):
    stock = django_filters.NumberFilter(field_name="stock", lookup_expr="iexact")
    product = django_filters.filters.ModelChoiceFilter(
        queryset=Product.objects.all()
    )
    # stock=models.IntegerField()
    # product = models.OneToOneField("Product",  on_delete=models.CASCADE, null=True)
    class Meta:
        model = Stock
        fields = '__all__'


class OrderFilter(django_filters.FilterSet):
    invoice = django_filters.CharFilter(field_name="invoice",lookup_expr='icontains',label="name")
    # product = django_filters.CharFilter(field_name="invoice",lookup_expr='icontains',label="name")
    product = django_filters.filters.ModelMultipleChoiceFilter(queryset=Product.objects.all())
    payment=django_filters.ModelChoiceFilter(queryset=Payment.objects.all())
    delivery=django_filters.ModelChoiceFilter(queryset=Delivery.objects.all())
    # invoice=models.CharField(max_length=30)
    # created=models.DateTimeField(auto_now=True)
    # is_paid=models.BooleanField(default=False)
    # destination=models.CharField(max_length=100)
    # product = models.ManyToManyField("Product")
    # payment=models.ForeignKey("Payment", on_delete=models.CASCADE, null=True)
    # delivery=models.ForeignKey("Delivery", on_delete=models.CASCADE, null=True)
    class Meta:
        model = Order
        fields = '__all__'


class CustomerFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    order=django_filters.ModelChoiceFilter(queryset=Order.objects.all())
    # first_name= models.CharField(max_length=30)
    # last_name= models.CharField(max_length=30)
    # email= models.EmailField()
    # image= models.ImageField(blank =True, null=True)
    # handphone= models.IntegerField()
    # address= models.CharField(max_length=100)
    # order=models.OneToOneField("Order",  on_delete=models.CASCADE, null=True)
    class Meta:
        model = Customer
        fields = '__all__'
        exclude= ['image']


class DeliveryFilter(django_filters.FilterSet):
    service = django_filters.CharFilter(lookup_expr='icontains')
    provider = django_filters.CharFilter(lookup_expr='icontains')

    # service= models.CharField(max_length=50)
    # provider= models.CharField(max_length=50, blank=True, null=True)
    # status=models.BooleanField(null=True)
    class Meta:
        model = Delivery
        fields = '__all__'


class PaymentFilter(django_filters.FilterSet):
    bank = django_filters.CharFilter(lookup_expr='icontains')


    # bank=models.CharField(max_length=20)
    # created=models.DateTimeField(auto_now=True)
    # status=models.BooleanField(null=True)
    class Meta:
        model = Payment
        fields = '__all__'