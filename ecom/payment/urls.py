from django.urls import path
from .import views

urlpatterns = [
    path('',views.payment_success,name='payment_success'),
    path('checkout',views.checkout,name='checkout'),
    path('billing_info',views.billing_info,name='billing_info'),
    path('process_order',views.process_order,name='process_order'),
    path('shipped_dash',views.shipped_dash,name='shipped_dash'),
    path('unshipped_dash',views.unshipped_dash,name='unshipped_dash'),
    path('orders<int:pk>',views.orders,name='orders'),
    
    
 ]
 