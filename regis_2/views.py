from django.shortcuts import render
from django.http import HttpResponse
from .models import course
# Create your views here.

def hello(request):
    data = course.objects.all()
    return render(request,'index.html',{'datas':data})