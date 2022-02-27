from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from tutorials.models import Customers
from tutorials.forms import CustomerForm

from tutorials.serializers import TutorialSerializer
from rest_framework.decorators import api_view

# Create your views here.
# def index(request):
#     return render(request, "tutorials/index.html")


def custList(request):  
    customers = Customers.objects.all()  
    return render(request,"tutorials/index.html",{'customers':customers})  

def custCreate(request):  
    if request.method == "POST":  
        form = CustomerForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('tutorials/index.html')  
            except:  
                pass  
    else:  
        form = CustomerForm()  
    return render(request,'tutorials/cust-create.html',{'form':form})  

def custUpdate(request, id):  
    customer = Customers.objects.get(customer_id=id)
    form = CustomerForm(initial={'customer_id': customer.customer_id, 'company_name': customer.company_name, 'contact_name': customer.contact_name, 'contact_title': customer.contact_title, 'address': customer.address, 'city': customer.city, 'region': customer.region, 'postal-code': customer.postal_code, 'country': customer.country, 'phone': customer.phone, 'fax': customer.fax })
    if request.method == "POST":  
        form = CustomerForm(request.POST, instance=customer)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('tutorials/index.html')  
            except Exception as e: 
                pass    
    return render(request,'tutorials/cust-update.html',{'form':form})  

def custDelete(request, id):
    customer = Customers.objects.get(customer_id=id)
    form = CustomerForm(initial={'name': customer.company_name, 'address': customer.address, 'city': customer.city})
    return render(request,'tutorials/cust-delete.html',{'form':form})  
