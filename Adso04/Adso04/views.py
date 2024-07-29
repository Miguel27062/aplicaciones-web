from django.http import HttpResponse

def index(request):
    return HttpResponse ("Hola mundo en Django")
from django.shortcuts import render

def index(request):
    return render(request,'index.html',{
        #context
    })