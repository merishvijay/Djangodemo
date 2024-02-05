from django.shortcuts import render
from shop.models import Product
from django.db.models import Q

def search(request):
    query=""
    products=None
    if(request.method=="POST"):
        query=request.POST['q']
        if(query):
            products=Product.objects.filter(Q(name_icontains=query)|Q(desc_icontains=query))
    return render(request,'search.html',{'query':query,'p':products})