from django.http import HttpResponse
from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def ppWovenFabrics(request):
    return render(request,'pp-woven-fabric.html')

def ppWovenBags(request):
    return render(request,'pp-woven-bags.html')

def contact(request):
    return render(request,'contact.html')