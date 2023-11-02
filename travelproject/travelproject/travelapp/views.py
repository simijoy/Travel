from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def demo(request):

    return render(request,'index.html')


def about(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    re=x+y
    x1=int(request.GET['num1'])
    y1=int(request.GET['num2'])
    re1=x1-y1
    x2= int(request.GET['num1'])
    y2= int(request.GET['num2'])
    re2 =x2*y2
    x3= int(request.GET['num1'])
    y3= int(request.GET['num2'])
    re3= x3/y3
    return render(request,'about.html',{'result':re,'result1':re1,'result2':re2,'result3':re3})
