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


def index(request):
    print("------------------------- I AM HERE")
    queryset = Customers.objects.all()
    return render(request, "tutorials/index.html", {'tutorials': queryset})


class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'tutorials/index.html'

    def get(self, request):
        queryset = Customers.objects.all()
        return Response({'tutorials': queryset})


class list_all_tutorials(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'tutorials/tutorial_list.html'

    def get(self, request):
        queryset = Customers.objects.all()
        return Response({'tutorials': queryset})

def custCreate(request):  
    if request.method == "POST":  
        form = CustomerForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('tutorial_list')  
            except:  
                pass  
    else:  
        form = CustomerForm()  
    return render(request,'cust-create.html',{'form':form})  

def custUpdate(request, id):  
    customer = Customers.objects.get(id=id)
    form = CustomerForm(initial={'name': customer.company_name, 'address': customer.address, 'city': customer.city})
    if request.method == "POST":  
        form = CustomerForm(request.POST, instance=customer)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('/tutorial_list')  
            except Exception as e: 
                pass    
    return render(request,'cust-update.html',{'form':form})  

def custDelete(request, id):
    customer = Customers.objects.get(id=id)
    try:
        customer.delete()
    except:
        pass
    return redirect('tutorial_list')
