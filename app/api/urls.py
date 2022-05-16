from django.urls import path, include
from app.api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('customer', views.CustomerViewSet, basename='CustomerViewSet')
router.register('order', views.OrderViewSet, basename='OrderViewSet')




urlpatterns = [
    path('api/', include(router.urls), name ='ApiCustomerViewSet' ),
]