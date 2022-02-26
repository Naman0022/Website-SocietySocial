from django.shortcuts import render
from .models import Member

# Create your views here.
def home(request):
    all_member = Member.objects.all
    return render(request,'home.html', {'all' : all_member})