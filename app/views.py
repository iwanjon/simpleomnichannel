from distutils.log import error
from errno import errorcode
from logging import exception
import os
# from sre_constants import SUCCESS
# from django import views
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views import View
from django.views.generic.edit import FormView, UpdateView, DeleteView
from requests import request
from django.http import JsonResponse
# from app.tasks import go_to_sleep, go_insert_data,save_product_from_csv
from app.tasks import *
from omnichannel.settings import BASE_DIR
from .models import *
from django.db.models import Q
from django.views.generic import TemplateView
from django_datatables_view.base_datatable_view import BaseDatatableView
from . forms import *
from .filters import *
from django.urls import reverse
import io, csv
# Create your views here.



def page_not_found(request, exception):
    return render(request, "404.html", {})

def server_error(request, exception=None):
    return render(request, "500.html", {})

def permission_denied(request, exception=None):
    return render(request, "403.html", {})

def bad_request(request, exception=None):
    return render(request, "400.html", {})




def data_json(Flist, Rreverse,EditUrl,DelUrl, Ccoldef):
    Flist["urll"]=reverse(Rreverse)
    Flist["coldef"] = Ccoldef
    Flist["datahead"]=[x["data"] for x in Flist["coldef"] ]
    Flist["editurl"]= reverse(EditUrl, args=(0,))
    Flist["deleteurl"]=reverse(DelUrl, args=(0,))


class CustomerListView(ListView):
    model = Customer
    template_name = "app/customer/customer.html"
    # ordering = ["-date"]
    
    context_object_name ="customers"
    
    def get_context_data(self, **kwargs):
        ret=super().get_context_data(**kwargs)
        # # print(ret, "makamkakm")
        return super().get_context_data(**kwargs)


class CustomerTableView(CustomerListView):
    template_name = "app/customer/customer-table.html" 
    title= "Customer"   
    
    def get_queryset(self):
        ret= super().get_queryset()
        self.filtered= CustomerFilter(self.request.GET,queryset=ret)
        return self.filtered.qs
    
    def get_context_data(self, **kwargs):
        ret =super().get_context_data(**kwargs)
        ret["filtered"] = self.filtered
        ret["title"] = self.title
        return ret

class CustomerDetailView(DetailView):
    model = Customer
    template_name = "app/customer/customer-detail.html"
    # ordering = ["-date"]

    context_object_name ="customer"
    # print(context_object_name)
    def get_context_data(self, **kwargs):
        data= super().get_context_data(**kwargs)
        # data["tags"] = self.object.tags.all()
        # members = [attr for attr in dir(data["object"]) if not callable(getattr(data["object"], attr)) and not attr.startswith("_")]
        # # print(data,"data")
        # data["pop_keys"]=["image", "image_name", "imagename"]
        # data["keys"]=[x for x in data["object"].__dict__.keys() if not x.startswith("_") and x not in data["pop_keys"]]
        # # print(data["object"].__dict__.items(),"data")
        # # print(data["object"].image.url,"data")
  
        
        data["data_dict"] ={k:v for k, v in data["object"].__dict__.items()
                            if not k.startswith("_") and k != "id"}
        # print(data["object"].__dict__.values(),"data")
        # print(data,"data")
        # data["comment_form"]= CommentForm()
        return data
    

class CustomerTableList(TemplateView):
    template_name = 'app/customertable.html'
    
    def get_context_data(self, **kwargs):
        ret= super().get_context_data(**kwargs)
        # # print(ret, "template engine")
        # ret["urll"] =r'{% url "customer-table-json" %}'
        # ret["urll"] =r'/customersjson/'
        # ret["urll"] =reverse("customer-table-json")
        # ret["coldef"]= [
   
        #     {
        #         "data": 'id',
        #         "targets": [0], 
        #     },
        #     {
        #         "data": 'first_name',
        #         "targets": [1]
        #     },
        #     {
        #         "data": 'email',
        #         "targets": [2]
        #     },
        #     {
        #         "data": 'last_name',
        #         "targets": [3]
        #     }
        # ]
        # ret["datahead"]=[x["data"] for x in ret["coldef"] ]
        Ccoldef= [
            {
                "data": 'id',
                "targets": [0], 
            },
            {
                "data": 'first_name',
                "targets": [1]
            },
            {
                "data": 'email',
                "targets": [2]
            },
            {
                "data": 'last_name',
                "targets": [3]
            },
            {
                "data": 'image',
                "targets": [4]
            },
            {
                "data": 'handphone',
                "targets": [5]
            },
            {
                "data": 'address',
                "targets": [6]
            },
            {
                "data": 'order',
                "targets": [7]
            }
        ]
        data_json(ret, "customer-table-json","customer-edit","customer-delete", Ccoldef)
        # print(ret,"after datajson")
        return ret

class CustomerTableListJson(BaseDatatableView):
    model = Customer
    columns = ['id', 'first_name', 'email', 'last_name', 'image', 'handphone', 'address', 'order']
    order_columns = ['email']

    # def filter_queryset(self, qs):
    #     sSearch = self.request.GET.get('sSearch', None)
    #     if sSearch:
    #         qs = qs.filter(Q(first_name__istartswith=sSearch) | Q(email__istartswith=sSearch))
    #     return qs


class Customer_Form(FormView):
    form_class=CustomerForm
    template_name="app/customer/customer-form.html"
    success_url ="/"

    
    # def post(self, request, *args, **kwargs):
    #     res= super().post(request, *args, **kwargs)
    #     res["email"]="nmnunu@gg.cc"
    #     # print(res,"post", self, "see",request,"rere",args,"args",kwargs)
    #     return res
    # def get_context_data(self, **kwargs):
    #     re= super().get_context_data(**kwargs)
    #     re["email"] = "ddd@gg.cc"
    #     return re
    
    # def get_form_kwargs(self):
    #     ret= super().get_form_kwargs()
    #     # print(ret,"form")
    #     return ret
    
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)


class CustomerEditForm(UpdateView):
    model = Customer
    form_class=CustomerForm
    # fields = '__all__'
    template_name = 'app/customer/customer-form.html'
    # context_object_name ="customer"
    success_url ="/"
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        id = self.object.id
        data["id"] = id
        # # print(data, "dddd", id, data["object"].email)
        # data["object"].email="siaaa@gg.cc"
        # data["customer"].email="siaaa@gg.cc"
        return data
    
    def get(self, request, *args, **kwargs):
        res= super().get(request, *args, **kwargs)
        # print(res,"rrrrr", self, "see",request,"rere",args,"args",kwargs)
        return res
    
    def post(self, request, *args, **kwargs):
        kwargs["last_name"]="nmnunu"
        res= super().post(request, *args, **kwargs)
        
        # print(res,"post", self, "see",request,"rere",args,"args",kwargs)
        return res
    
    def get_form_kwargs(self):
        ret= super().get_form_kwargs()
        # print(ret,"form")
        # print(ret["instance"].email,"fff")
        ret["instance"].email= "qqq@qq.cc"
        return ret
    
    def form_valid(self, form):
        ret = super().form_valid(form)
        #  binding instance for form 
        xx = form.save(commit=False)
        xx.email="mamam@gg.cc"
        print(ret, "fff",self,"fff", form,"dfdfdf",xx)
        xx.save()
        return ret
        
# activity = Activity.objects.get(id=id)
# form = ActivityGoalForm(request.POST)
# if form.is_valid():
#     #use commit = false, set other excluded fields, and then save object
#     obj = form.save(commit=False)
#     obj.activity = activity
#     obj.save()

class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = "/"
    template_name = 'app/customer/customer-form.html'
    
    def get_context_data(self, **kwargs):
        ret= super().get_context_data(**kwargs)
        ret["is_delete"] = True
        # # print("wer",kwargs,"der",self)
        return ret
        
    def get_context_object_name(self, obj):
        ret= super().get_context_object_name(obj)
        # print(obj, "obj", self)
        return ret

####################################################################################
### Product

class ProductListView(ListView):
    model = Product
    template_name = "app/product/product.html"
    
    def get_context_data(self, **kwargs):
        # # print(super().get_context_data(**kwargs), "makamkakm")
        return super().get_context_data(**kwargs)


class ProductTableView(ProductListView):
    template_name = "app/product/product-table.html" 
    title= "Product"   
    
    def get_queryset(self):
        ret= super().get_queryset()
        self.filtered= ProductFilter(self.request.GET,queryset=ret)
        return self.filtered.qs
    
    def get_context_data(self, **kwargs):
        ret =super().get_context_data(**kwargs)
        print(ret,"test", self )
        ret["filtered"] = self.filtered
        ret["title"] = self.title
        return ret



class ProductDetailView(DetailView):
    model = Product
    template_name = "app/product/product-detail.html"
    # ordering = ["-date"]

    # context_object_name ="customer"
    # # print(context_object_name)
    def get_context_data(self, **kwargs):
        data= super().get_context_data(**kwargs)
  
        data["data_dict"] ={k:v for k, v in data["object"].__dict__.items()
                            if not k.startswith("_") and k != "id"}
        # # print(data["object"].__dict__.values(),"data")
        # # print(data,"data")
        return data
    

class ProductTableList(TemplateView):
    template_name = 'app/customertable.html'
    
    def get_context_data(self, **kwargs):
        ret= super().get_context_data(**kwargs)
        # # print(ret, "template engine")
        Ccoldef= [
            {
                "data": 'id',
                "targets": [0], 
            },
            {
                "data": 'name',
                "targets": [1]
            },
            {
                "data": 'code',
                "targets": [2]
            },
            {
                "data": 'channel',
                "targets": [3]
            },
            {
                "data": 'status',
                "targets": [4]
            }
        ]
        data_json(ret, "product-table-json","product-edit","product-delete", Ccoldef)
        # # print(ret,"after datajson")
        return ret

class ProductTableListJson(BaseDatatableView):
    model = Product
    columns = ['id', 'name', 'code', 'channel', 'status'] 
   
    
    def get_context_data(self, *args, **kwargs):
        ret= super().get_context_data(*args, **kwargs)
        # print(ret)
        return ret

class Product_Form(FormView):
    form_class=ProductForm
    template_name="app/product/product-form.html"
    success_url ="/"
    
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)


class ProductEditForm(UpdateView):
    model = Product
    form_class= ProductForm
    template_name = 'app/product/product-form.html'
    success_url ="/"
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        id = self.object.id
        data["id"] = id
        # print(data, "dddd", id, data["object"])
        return data
    
    
    def get_form_kwargs(self):
        ret= super().get_form_kwargs()
        # print(ret,"form")
        # print(ret["instance"],"fff")
        return ret
    
    def form_valid(self, form):
        ret = super().form_valid(form)
        #  binding instance for form 
        xx = form.save(commit=False)
        # print(ret, "fff",self,"fff", form,"dfdfdf",xx)
        xx.save()
        return ret
        

class ProductDeleteView(DeleteView):
    model = Product
    success_url = "/"
    template_name = 'app/product/product-form.html'
    
    def get_context_data(self, **kwargs):
        ret= super().get_context_data(**kwargs)
        ret["is_delete"] = True
        # print("wer",kwargs,"der",self)
        return ret
        
    def get_context_object_name(self, obj):
        ret= super().get_context_object_name(obj)
        # print(obj, "obj", self)
        return ret





####################################################################################
### Order

class OrderListView(ListView):
    model = Order
    template_name = "app/order/order.html"
    
    def get_context_data(self, **kwargs):
        # print(super().get_context_data(**kwargs), "makamkakm")
        ret= super().get_context_data(**kwargs)
        # print(ret, "this is ter")
        return ret


class OrderTableView(OrderListView):
    template_name = "app/order/order-table.html" 
    title= "Order"   
    
    def get_queryset(self):
        ret= super().get_queryset()
        self.filtered= OrderFilter(self.request.GET,queryset=ret)
        return self.filtered.qs
    
    
    def get_context_data(self, **kwargs):
        ret =super().get_context_data(**kwargs)
        # print(ret, "try",self)
        ret["filtered"] = self.filtered
        ret["title"] = self.title
        return ret


class OrderDetailView(DetailView):
    model = Order
    template_name = "app/order/order-detail.html"
    # ordering = ["-date"]

    # context_object_name ="customer"
    # # print(context_object_name)
    def get_context_data(self, **kwargs):
        data= super().get_context_data(**kwargs)
  
        data["data_dict"] ={k:v for k, v in data["object"].__dict__.items()
                            if not k.startswith("_") and k != "id"}
        # print(data["object"].__dict__.values(),"data")
        # print(data,"data")
        return data
    

class OrderTableList(TemplateView):
    template_name = 'app/customertable.html'
    
    def get_context_data(self, **kwargs):
        ret= super().get_context_data(**kwargs)
        # print(ret, "template engine")
        Ccoldef= [
            {
                "data": 'id',
                "targets": [0], 
            },
            {
                "data": 'invoice',
                "targets": [1]
            },
            {
                "data": 'created',
                "targets": [2]
            },
            {
                "data": 'is_paid',
                "targets": [3]
            },
            {
                "data": 'destination',
                "targets": [4]
            },
            {
                "data": 'product',
                "targets": [5]
            },
            {
                "data": 'payment',
                "targets": [6]
            },
            {
                "data": 'delivery',
                "targets": [7]
            }
        ]  #['id', 'invoice', 'created', 'is_paid', 'destination', 'product', 'payment', 'delivery'] 
        data_json(ret, "order-table-json","order-edit","order-delete", Ccoldef)
        # print(ret,"after datajson")
        return ret

class OrderTableListJson(BaseDatatableView):
    model = Order
    columns = ['id', 'invoice', 'created', 'is_paid', 'destination', 'product', 'payment', 'delivery'] 
   
    
    def get_context_data(self, *args, **kwargs):
        ret= super().get_context_data(*args, **kwargs)
        # print(ret)
        return ret

class Order_Form(FormView):
    form_class=OrderForm
    template_name="app/order/order-form.html"
    success_url ="/"
    
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)


class OrderEditForm(UpdateView):
    model = Order
    form_class= OrderForm
    template_name = 'app/order/order-form.html'
    success_url ="/"
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        id = self.object.id
        data["id"] = id
        # print(data, "dddd", id, data["object"])
        return data
    
    
    def get_form_kwargs(self):
        ret= super().get_form_kwargs()
        # print(ret,"form")
        # print(ret["instance"],"fff")
        return ret
    

    
    def form_valid(self, form):
        ret = super().form_valid(form)
        #  binding instance for form 
        
        xx = form.save(commit=False)
        ee=Order.objects.get(pk=xx.id)
        # for aai in ee.product.all():
        #     if aai.stock.stock == 10:
        #         print("this event")
        #         # raise Exception('OMG')
        #         # return HttpResponseRedirect(self.get_success_url())
        #         return self.form_invalid(form)
        print(ret, "fff",self,"fff", form,"dfdfdf",xx, xx.id, ee)
        print(ee.product,"product from oreder")
        print(ee.product.all()[0],"productr")
        print(ee.product.all()[0].stock.stock,"mongo")
        xx.save()
        return ret
        


class OrderDeleteView(DeleteView):
    model = Order
    success_url = "/"
    template_name = 'app/order/order-form.html'
    
    def get_context_data(self, **kwargs):
        ret= super().get_context_data(**kwargs)
        ret["is_delete"] = True
        # print("wer",kwargs,"der",self)
        return ret
        
    def get_context_object_name(self, obj):
        ret= super().get_context_object_name(obj)
        # print(obj, "obj", self)
        return ret






####################################################################################
### Delivery

class DeliveryListView(ListView):
    model = Delivery
    template_name = "app/delivery/delivery.html"
    
    def get_context_data(self, **kwargs):
        ret = super().get_context_data(**kwargs)
  
        return ret


class DeliveryTableView(DeliveryListView):
    template_name = "app/delivery/delivery-table.html" 
    title= "Delivery"   
    
    def get_queryset(self):
        ret= super().get_queryset()
        self.filtered= DeliveryFilter(self.request.GET,queryset=ret)
        return self.filtered.qs
    
    def get_context_data(self, **kwargs):
        ret =super().get_context_data(**kwargs)
        ret["filtered"] = self.filtered
        ret["title"] = self.title
        return ret

class DeliveryDetailView(DetailView):
    model = Delivery
    template_name = "app/delivery/delivery-detail.html"
    # deliverying = ["-date"]

    # context_object_name ="customer"
    # # print(context_object_name)
    def get_context_data(self, **kwargs):
        data= super().get_context_data(**kwargs)
  
        data["data_dict"] ={k:v for k, v in data["object"].__dict__.items()
                            if not k.startswith("_") and k != "id"}
        # print(data["object"].__dict__.values(),"data")
        # print(data,"data")
        return data
    

class DeliveryTableList(TemplateView):
    template_name = 'app/customertable.html'
    
    def get_context_data(self, **kwargs):
        ret= super().get_context_data(**kwargs)
        # print(ret, "template engine")
        Ccoldef= [
            {
                "data": 'id',
                "targets": [0], 
            },
            {
                "data": 'provider',
                "targets": [1]
            },
            {
                "data": 'service',
                "targets": [2]
            },
            {
                "data": 'status',
                "targets": [3]
            }
        ]  #['id', 'invoice', 'created', 'is_paid', 'destination', 'product', 'payment', 'delivery'] 
        data_json(ret, "delivery-table-json","delivery-edit","delivery-delete", Ccoldef)
        # print(ret,"after datajson")
        return ret

class DeliveryTableListJson(BaseDatatableView):
    model = Delivery
    columns = ['id', 'provider', 'service', 'status'] 
   
    
    def get_context_data(self, *args, **kwargs):
        ret= super().get_context_data(*args, **kwargs)
        # print(ret)
        return ret

class Delivery_Form(FormView):
    form_class=DeliveryForm
    template_name="app/delivery/delivery-form.html"
    success_url ="/"
    
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)


class DeliveryEditForm(UpdateView):
    model = Delivery
    form_class= DeliveryForm
    template_name = 'app/delivery/delivery-form.html'
    success_url ="/"
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        id = self.object.id
        data["id"] = id
        # print(data, "dddd", id, data["object"])
        return data
    
    
    def get_form_kwargs(self):
        ret= super().get_form_kwargs()
        # print(ret,"form")
        # print(ret["instance"],"fff")
        return ret
    
    def form_valid(self, form):
        ret = super().form_valid(form)
        #  binding instance for form 
        xx = form.save(commit=False)
        # print(ret, "fff",self,"fff", form,"dfdfdf",xx)
        xx.save()
        return ret
        

class DeliveryDeleteView(DeleteView):
    model = Delivery
    success_url = "/"
    template_name = 'app/delivery/delivery-form.html'
    
    def get_context_data(self, **kwargs):
        ret= super().get_context_data(**kwargs)
        ret["is_delete"] = True
        # print("wer",kwargs,"der",self)
        return ret
        
    def get_context_object_name(self, obj):
        ret= super().get_context_object_name(obj)
        # print(obj, "obj", self)
        return ret





####################################################################################
### Stock

class StockListView(ListView):
    model = Stock
    template_name = "app/stock/stock.html"
    
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)




class StockTableView(StockListView):
    template_name = "app/stock/stock-table.html" 
    title= "Stock"   
    
    def get_queryset(self):
        ret= super().get_queryset()
        self.filtered= StockFilter(self.request.GET,queryset=ret)
        return self.filtered.qs
    
    def get_context_data(self, **kwargs):
        ret =super().get_context_data(**kwargs)
        ret["filtered"] = self.filtered
        ret["title"] = self.title
        return ret


class StockDetailView(DetailView):
    model = Stock
    template_name = "app/stock/stock-detail.html"
    # stocking = ["-date"]

    # context_object_name ="customer"
    # # print(context_object_name)
    def get_context_data(self, **kwargs):
        data= super().get_context_data(**kwargs)
  
        data["data_dict"] ={k:v for k, v in data["object"].__dict__.items()
                            if not k.startswith("_") and k != "id"}
        # print(data["object"].__dict__.values(),"data")
        # print(data,"data")
        return data
    

class StockTableList(TemplateView):
    template_name = 'app/customertable.html'
    
    def get_context_data(self, **kwargs):
        ret= super().get_context_data(**kwargs)
        # print(ret, "template engine")
        Ccoldef= [
            {
                "data": 'id',
                "targets": [0], 
            },
            {
                "data": 'stock',
                "targets": [1]
            },
            {
                "data": 'product',
                "targets": [2]
            }
        ]  #['id', 'invoice', 'created', 'is_paid', 'destination', 'product', 'payment', 'stock'] 
        data_json(ret, "stock-table-json","stock-edit","stock-delete", Ccoldef)
        # print(ret,"after datajson")
        return ret

class StockTableListJson(BaseDatatableView):
    model = Stock
    columns = ['id', 'stock', 'product'] 
   
    
    def get_context_data(self, *args, **kwargs):
        ret= super().get_context_data(*args, **kwargs)
        # print(ret)
        return ret

class Stock_Form(FormView):
    form_class=StockForm
    template_name="app/stock/stock-form.html"
    success_url ="/"
    
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)


class StockEditForm(UpdateView):
    model = Stock
    form_class= StockForm
    template_name = 'app/stock/stock-form.html'
    success_url ="/"
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        id = self.object.id
        data["id"] = id
        # # print(data, "dddd", id, data["object"])
        return data
    
    
    def get_form_kwargs(self):
        ret= super().get_form_kwargs()
        # # print(ret,"form")
        # # print(ret["instance"],"fff")
        return ret
    
    def form_valid(self, form):
        ret = super().form_valid(form)
        #  binding instance for form 
        xx = form.save(commit=False)
        # print(ret, "fff",self,"fff", form,"dfdfdf",xx)
        xx.save()
        return ret
        

class StockDeleteView(DeleteView):
    model = Stock
    success_url = "/"
    template_name = 'app/stock/stock-form.html'
    
    def get_context_data(self, **kwargs):
        ret= super().get_context_data(**kwargs)
        ret["is_delete"] = True
        # # print("wer",kwargs,"der",self)
        return ret
        
    def get_context_object_name(self, obj):
        ret= super().get_context_object_name(obj)
        # # print(obj, "obj", self)
        return ret



####################################################################################
### Payment

class PaymentListView(ListView):
    model = Payment
    template_name = "app/payment/payment.html"
    
    def get_context_data(self, **kwargs):
        # # print(super().get_context_data(**kwargs), "makamkakm")
        return super().get_context_data(**kwargs)


class PaymentTableView(PaymentListView):
    template_name = "app/payment/payment-table.html" 
    title= "Payment"   
    
    def get_queryset(self):
        ret= super().get_queryset()
        self.filtered= PaymentFilter(self.request.GET,queryset=ret)
        return self.filtered.qs
    
    def get_context_data(self, **kwargs):
        ret =super().get_context_data(**kwargs)
        ret["filtered"] = self.filtered
        ret["title"] = self.title
        return ret




class PaymentDetailView(DetailView):
    model = Payment
    template_name = "app/payment/payment-detail.html"
    # paymenting = ["-date"]

    # context_object_name ="customer"
    # # print(context_object_name)
    def get_context_data(self, **kwargs):
        data= super().get_context_data(**kwargs)
  
        data["data_dict"] ={k:v for k, v in data["object"].__dict__.items()
                            if not k.startswith("_") and k != "id"}
        # # print(data["object"].__dict__.values(),"data")
        # # print(data,"data")
        return data
    

class PaymentTableList(TemplateView):
    template_name = 'app/customertable.html'
    
    def get_context_data(self, **kwargs):
        ret= super().get_context_data(**kwargs)
        # # print(ret, "template engine")
        Ccoldef= [
            {
                "data": 'id',
                "targets": [0], 
            },
            {
                "data": 'bank',
                "targets": [1]
            },
            {
                "data": 'created',
                "targets": [2]
            },
            {
                "data": 'status',
                "targets": [3]
            }
        ]  #['id', 'invoice', 'created', 'is_paid', 'destination', 'product', 'payment', 'payment'] 
        data_json(ret, "payment-table-json","payment-edit","payment-delete", Ccoldef)
        # print(ret,"after datajson")
        return ret

class PaymentTableListJson(BaseDatatableView):
    model = Payment
    columns = ['id', 'bank', 'created', 'status'] 
   
    
    def get_context_data(self, *args, **kwargs):
        ret= super().get_context_data(*args, **kwargs)
        # # print(ret)
        return ret

class Payment_Form(FormView):
    form_class=PaymentForm
    template_name="app/payment/payment-form.html"
    success_url ="/"
    
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)


class PaymentEditForm(UpdateView):
    model = Payment
    form_class= PaymentForm
    template_name = 'app/payment/payment-form.html'
    success_url ="/"
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        id = self.object.id
        data["id"] = id
        # # print(data, "dddd", id, data["object"])
        return data
    
    
    def get_form_kwargs(self):
        ret= super().get_form_kwargs()
        # print(ret,"form")
        # print(ret["instance"],"fff")
        return ret
    
    def form_valid(self, form):
        ret = super().form_valid(form)
        #  binding instance for form 
        xx = form.save(commit=False)
        # print(ret, "fff",self,"fff", form,"dfdfdf",xx)
        xx.save()
        return ret
        

class PaymentDeleteView(DeleteView):
    model = Payment
    success_url = "/"
    template_name = 'app/payment/payment-form.html'
    
    def get_context_data(self, **kwargs):
        ret= super().get_context_data(**kwargs)
        ret["is_delete"] = True
        # # print("wer",kwargs,"der",self)
        return ret
        
    def get_context_object_name(self, obj):
        ret= super().get_context_object_name(obj)
        # print(obj, "obj", self)
        return ret




####################################################################################
### Channel

class ChannelListView(ListView):
    model = Channel
    template_name = "app/channel/channel.html"
    paginate_by = 1
    
    def get_context_data(self, **kwargs):
        # # print(super().get_context_data(**kwargs), "makamkakm")
        return super().get_context_data(**kwargs)


class ChannelTableView(ChannelListView):
    template_name ="app/channel/channel-table.html"
    title = "Channel"
    
    def get_queryset(self):
        ret= super().get_queryset()
        # ret2=self.model.objects.all()
        # # print(ret,"alll rest", ret2)
        filtered = ChannelFilter(self.request.GET, queryset=ret)
        self.filtered=filtered
        # # print(filtered, "all", filtered.qs)
        return filtered.qs
    
    def get_context_data(self, **kwargs):
        ret= super().get_context_data(**kwargs)
        ret["filtered"]= self.filtered
        ret["title"]= self.title
        # # print(ret,"get data", self.__dict__, self.filtered)
        return ret

class ChannelDetailView(DetailView):
    model = Channel
    template_name = "app/channel/channel-detail.html"
    # channeling = ["-date"]

    # context_object_name ="customer"
    # # print(context_object_name)
    def get_context_data(self, **kwargs):
        data= super().get_context_data(**kwargs)
  
        data["data_dict"] ={k:v for k, v in data["object"].__dict__.items()
                            if not k.startswith("_") and k != "id"}
        # # print(data["object"].__dict__.values(),"data")
        # # print(data,"data")
        return data
    

class ChannelTableList(TemplateView):
    template_name = 'app/customertable.html'
    
    def get_context_data(self, **kwargs):
        ret= super().get_context_data(**kwargs)
        # # print(ret, "template engine")
        Ccoldef= [
            {
                "data": 'id',
                "targets": [0], 
            },
            {
                "data": 'name',
                "targets": [1]
            },
            {
                "data": 'status',
                "targets": [2]
            }
        ]  #['id', 'invoice', 'created', 'is_paid', 'destination', 'product', 'channel', 'channel'] 
        data_json(ret, "channel-table-json","channel-edit","channel-delete", Ccoldef)
        # print(ret,"after datajson")
        return ret

class ChannelTableListJson(BaseDatatableView):
    model = Channel
    columns = ['id', 'name',  'status'] 
   
    
    def get_context_data(self, *args, **kwargs):
        ret= super().get_context_data(*args, **kwargs)
        # # print(ret)
        return ret

class Channel_Form(FormView):
    form_class=ChannelForm
    template_name="app/channel/channel-form.html"
    success_url ="/"
    
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)


class ChannelEditForm(UpdateView):
    model = Channel
    form_class= ChannelForm
    template_name = 'app/channel/channel-form.html'
    success_url ="/"
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        id = self.object.id
        data["id"] = id
        # # print(data, "dddd", id, data["object"])
        return data
    
    
    def get_form_kwargs(self):
        ret= super().get_form_kwargs()
        # print(ret,"form")
        # print(ret["instance"],"fff")
        return ret
    
    def form_valid(self, form):
        ret = super().form_valid(form)
        #  binding instance for form 
        xx = form.save(commit=False)
        # print(ret, "fff",self,"fff", form,"dfdfdf",xx)
        xx.save()
        return ret
        

class ChannelDeleteView(DeleteView):
    model = Channel
    success_url = "/"
    template_name = 'app/channel/channel-form.html'
    
    def get_context_data(self, **kwargs):
        ret= super().get_context_data(**kwargs)
        ret["is_delete"] = True
        # # print("wer",kwargs,"der",self)
        return ret
        
    def get_context_object_name(self, obj):
        ret= super().get_context_object_name(obj)
        # print(obj, "obj", self)
        return ret
    
    
####################################################################################
### Upload ajax
####################################################################################
### just trial

def uploadFIle(request):
    form=UploadForm()
    template = 'app/upload/upload.html'
    prompt={
        "order":"order of csv must bla bla bla"
    }

    if request.method== 'GET':
        return render(request, template, {"form":form})
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
    csv_file = "empty"
    if form.is_valid():
        print(form.cleaned_data)
        # csv_file = form.cleaned_data['csv_file']
    
    print(request,"rererer", form, request.POST, csv_file)
    csv_file=request.FILES['file']
    dataset=csv_file.read().decode('UTF-8')
    io_string=io.StringIO(dataset)
    next(io_string)
    for col in csv.reader(io_string, delimiter=',',quotechar="|"):
        print(col)
        xx,created=Product.objects.update_or_create(
            name=col[0],
            code=col[1],
            channel=Channel.objects.get(pk=int(col[2])),
            status= int(col[3])
        )
        # _,created = Contact.object.update_or_create(
        #     co=col[0],
        #     cc=col[1]
        # )
        
    context ={}
    return render(request, template,  {"form":form})

    
####################################################################################
### Upload-celery
####################################################################################
### just trial

def uploadFIleCelery(request):
    form=UploadForm()
    template = 'app/upload/upload_celery.html'
    prompt={
        "order":"order of csv must bla bla bla"
    }

    if request.method== 'GET':
        return render(request, template, {"form":form})
    if request.method == 'POST':
        # task = go_to_sleep.delay(1)
        # print(task,task.task_id,"uiuiuiuuiu")
        form = UploadForm(request.POST, request.FILES)
    csv_file = "empty"
    if form.is_valid():
        print(form.cleaned_data)
        # csv_file = form.cleaned_data['csv_file']
        print(os.path,"filepath")
        handle_uploaded_file(request.FILES['file'])
        print(BASE_DIR,"filepath")
        print(request.FILES['file'],"filepathsws")
        file_path = os.path.join(BASE_DIR, "media",str(request.FILES['file']))
        print(file_path,"filepath")
        
    task=save_product_from_csv.delay(file_path)

    return JsonResponse({ 'task_id' : task.task_id})




####################################################################################
### celery
####################################################################################
### just trail

def index(request):
    task = go_to_sleep.delay(1)
    return render(request, 'app/index.html', {'task_id' : task.task_id})




####################################################################################
### Upload-celery

class UploadFileCeleryCLass(View):
    form=UploadForm()
    template = 'app/upload/upload_celery.html'
    
    def get(self, request):
        return render(request, self.template, {"form":self.form})
        
    def post(self,request):
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            print(form.cleaned_data)
            print(os.path,"filepath")
            
            handle_uploaded_file(request.FILES['file'])
            print(BASE_DIR,"filepath")
            print(request.FILES['file'],"filepathsws")
            
            file_path = os.path.join(BASE_DIR, "media",str(request.FILES['file']))
            print(file_path,"filepath")
            
            is_header=check_header(file_path)
            
            if not is_header:
                return JsonResponse({'status':'false','message':"invalid header, header must be 'name','code','channel','status' sequentially"},status=400)
            
            task=save_product_from_csv.delay(file_path)
            return JsonResponse({ 'task_id' : task.task_id})
        
        return JsonResponse({"message":"invalid form data", "status":400},status=400)
        


def check_header(file_path):
    
    with open(file_path, 'r') as fp:
        productss = csv.reader(fp, delimiter=',')
        header=next(productss)
        print(header, " this is header")
        fp.close()
        
    if header != ['name','code','channel','status']:
        return False

    return True

def handle_uploaded_file(f):
    with open('media/'+str(f), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)