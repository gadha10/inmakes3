from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Create your views here.
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from.models import place
from.models import person
# Create your views here.
# def home(request):
#    return render (request,"home.html")
# def about(request):
#    return HttpResponse("I am inmakes student")
# def contact(request):
#    return render (request,"detail.html")
# def details(request):
#    return render (request,"details.html")
# def thanks(request):
#    return HttpResponse ("Thank u all")
# def home(request):
#    return HttpResponse("Hello world")
# def home(request):
#     return render(request,"inp.html")
#
# def opr(request):
#    x=int(request.GET['number1'])
#    y= int(request.GET['number2'])
#    r1=x+y
#    r2=x-y
#    r3=x*y
#    r4=x/y
#    return render(request,"result.html",{'result1':r1,
#                                         'result2':r2,
#                                         'result3':r3,
#                                         'result4':r4})

def home1(request):
     obj1=place.objects.all()
     obj2 = person.objects.all()
     return render(request,"index.html",{'result':obj1,'result1':obj2})


