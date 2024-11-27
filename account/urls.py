from django.urls import path
from .views import *

urlpatterns=[
    path('',home,name='home'),
    path('product/',products,name='products'),
    path('customer/<str:pk>/',customer,name='customer'),
    path('create_order/',createOrder,name='create_order'),
    path('update_order/<str:pk>/',updateOrder,name='update_order')
]