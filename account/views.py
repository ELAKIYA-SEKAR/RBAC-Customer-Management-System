from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def home(request):
    orders=Order.objects.all()
    customer=Customer.objects.all()
    total_customer=customer.count()
    total_orders=orders.count()
    delivered=orders.filter(status='Delivered').count()
    pending=orders.filter(status='Pending').count()

    context={'orders':orders,"customer":customer,'total_orders':total_orders,
             'delivered':delivered,'pending':pending}
    
    return render(request,'account/dashboard.html',context)

def products(request):
    products=Product.objects.all()

    return render(request,'account/products.html',{'products':products})

def customer(request,pk):
    customer=Customer.objects.get(id=pk)
    orders=customer.order_set.all()
    total_orders=orders.count()

    context={"customer":customer,'orders':orders,'total_orders':total_orders}
    return render(request,'account/customer.html',context)

def createOrder(request):
    form=OrderForms()
    if request.method=='POST':
        form=OrderForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context={'form':form}
    return render(request,'account/order_form.html',context)

def updateOrder(request,pk):
    order=Order.objects.get(id=pk)
    form=OrderForms(instance=order)
    if request.method=='POST':
        form=OrderForms(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'form':form}
    return render(request,'account/order_form.html',context)
