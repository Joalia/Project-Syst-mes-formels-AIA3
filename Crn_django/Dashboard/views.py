from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def list_dash(request):
    return render(request,'Dashboard/dashboard.html')