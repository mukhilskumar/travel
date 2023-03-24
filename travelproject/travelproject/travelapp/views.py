from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from  .models import People

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    res=People.objects.all()
    return render(request,"index.html",{'result':obj,'result1':res})
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     res1=x-y
#     res2=x*y
#     res3=x/y
#     return render(request,"about.html",{'result':res,'result1':res1,'result2':res2,'result3':res3})