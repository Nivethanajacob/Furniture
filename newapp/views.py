from django.shortcuts import render, redirect, get_object_or_404
from .models import Order

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def form(request):
    return render(request, 'form.html')

def insertuser(request):
    if request.method == "POST":
        Order.objects.create(
            customer_name=request.POST['customer_name'],
            email=request.POST['email'],
            contact=request.POST['contact'],
            product=request.POST['product'],
            quantity=request.POST['quantity'],
            address=request.POST['address'],
            payment_method=request.POST['payment_method']
        )
        return redirect('success')
    return redirect('form')

def success(request):
    return render(request, 'success.html')

