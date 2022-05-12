from django.urls import path
from app import views

urlpatterns = [
    path('', views.CustomerListView.as_view(), name="customer-list-view"),
    path('customers/', views.CustomerTableList.as_view(), name="customer-table-list"),
    path('customer-table/', views.CustomerTableView.as_view(), name="customer-table-view"),
    path('customersjson/', views.CustomerTableListJson.as_view(), name="customer-table-json"),
    path('customer/<int:pk>/', views.CustomerDetailView.as_view(), name="customer-detail"),
    path('customer/<int:pk>/delete', views.CustomerDeleteView.as_view(), name="customer-delete"),
    path('customer/<int:pk>/edit', views.CustomerEditForm.as_view(), name="customer-edit"),
    path('customer-form/', views.Customer_Form.as_view(), name="customer-form"),
    # path('customer/<int:pk>', views.CustomerDetailView.as_view(), name="customer-detail"),
    # path('posts/',views.posts_page_class.as_view(), name="posts-page"),
    # path('posts/<slug:slug>',views.postDetailView.as_view() ,  name ="post-detail-page"),
    # path('read-later',views.ReadLaterView.as_view() ,  name ="read-later")
    path('product/', views.ProductListView.as_view(), name="product-list-view"),
    path('product-table/', views.ProductTableView.as_view(), name="product-table-view"),
    path('products/', views.ProductTableList.as_view(), name="product-table-list"),
    path('productsjson/', views.ProductTableListJson.as_view(), name="product-table-json"),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name="product-detail"),
    path('product/<int:pk>/delete', views.ProductDeleteView.as_view(), name="product-delete"),
    path('product/<int:pk>/edit', views.ProductEditForm.as_view(), name="product-edit"),
    path('product-form/', views.Product_Form.as_view(), name="product-form"),
    ##########################
    ##########################
    ##########################
    path('order/', views.OrderListView.as_view(), name="order-list-view"),
    path('orders/', views.OrderTableList.as_view(), name="order-table-list"),
    path('order-table/', views.OrderTableView.as_view(), name="order-table-view"),
    path('ordersjson/', views.OrderTableListJson.as_view(), name="order-table-json"),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name="order-detail"),
    path('order/<int:pk>/delete', views.OrderDeleteView.as_view(), name="order-delete"),
    path('order/<int:pk>/edit', views.OrderEditForm.as_view(), name="order-edit"),
    path('order-form/', views.Order_Form.as_view(), name="order-form"),
    ##########################
    ##########################
    ##########################
    path('delivery/', views.DeliveryListView.as_view(), name="delivery-list-view"),
    path('deliverys/', views.DeliveryTableList.as_view(), name="delivery-table-list"),
    path('delivery-table/', views.DeliveryTableView.as_view(), name="delivery-table-view"),
    path('deliverysjson/', views.DeliveryTableListJson.as_view(), name="delivery-table-json"),
    path('delivery/<int:pk>/', views.DeliveryDetailView.as_view(), name="delivery-detail"),
    path('delivery/<int:pk>/delete', views.DeliveryDeleteView.as_view(), name="delivery-delete"),
    path('delivery/<int:pk>/edit', views.DeliveryEditForm.as_view(), name="delivery-edit"),
    path('delivery-form/', views.Delivery_Form.as_view(), name="delivery-form"),
    ##########################
    ##########################
    ##########################
    path('channel/', views.ChannelListView.as_view(), name="channel-list-view"),
    path('channel-table/', views.ChannelTableView.as_view(), name="channel-table-view"),
    path('channels/', views.ChannelTableList.as_view(), name="channel-table-list"),
    path('channelsjson/', views.ChannelTableListJson.as_view(), name="channel-table-json"),
    path('channel/<int:pk>/', views.ChannelDetailView.as_view(), name="channel-detail"),
    path('channel/<int:pk>/delete', views.ChannelDeleteView.as_view(), name="channel-delete"),
    path('channel/<int:pk>/edit', views.ChannelEditForm.as_view(), name="channel-edit"),
    path('channel-form/', views.Channel_Form.as_view(), name="channel-form"),
    ##########################
    ##########################
    ##########################
    path('payment/', views.PaymentListView.as_view(), name="payment-list-view"),
    path('payments/', views.PaymentTableList.as_view(), name="payment-table-list"),
    path('payment-table/', views.PaymentTableView.as_view(), name="payment-table-view"),
    path('paymentsjson/', views.PaymentTableListJson.as_view(), name="payment-table-json"),
    path('payment/<int:pk>/', views.PaymentDetailView.as_view(), name="payment-detail"),
    path('payment/<int:pk>/delete', views.PaymentDeleteView.as_view(), name="payment-delete"),
    path('payment/<int:pk>/edit', views.PaymentEditForm.as_view(), name="payment-edit"),
    path('payment-form/', views.Payment_Form.as_view(), name="payment-form"),
    ##########################
    ##########################
    ##########################
    path('stock/', views.StockListView.as_view(), name="stock-list-view"),
    path('stocks/', views.StockTableList.as_view(), name="stock-table-list"),
    path('stock-table/', views.StockTableView.as_view(), name="stock-table-view"),
    path('stocksjson/', views.StockTableListJson.as_view(), name="stock-table-json"),
    path('stock/<int:pk>/', views.StockDetailView.as_view(), name="stock-detail"),
    path('stock/<int:pk>/delete', views.StockDeleteView.as_view(), name="stock-delete"),
    path('stock/<int:pk>/edit', views.StockEditForm.as_view(), name="stock-edit"),
    path('stock-form/', views.Stock_Form.as_view(), name="stock-form"),
    ##########################
    ##########################
    ##########################
    path('upload-form/', views.uploadFIle, name="upload-form"),
    path('upload-form-celery/', views.UploadFileCeleryCLass.as_view(), name="upload-form-celery"),
    path('upload-twet/', views.index, name="index"),
]