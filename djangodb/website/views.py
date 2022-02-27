from django.shortcuts import render
from .models import Member

# Create your views here.
def index(request):  
    return render(request,'index.html', {})
def registration_community(request):
    return render(request,'registration_community.html', {})