from django.shortcuts import render
from .models import Member

# Create your views here.
def index(request):  
    return render(request,'index.html', {})
def join(request):
    return render(request,'join.html', {})