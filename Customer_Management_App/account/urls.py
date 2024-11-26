from django.urls import path
from .views import *

urlpatterns=[
    path('',home),
    path('product/',products),
    path('customer/',customer)
]