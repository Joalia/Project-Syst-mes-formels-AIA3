from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def cardio(request):
    return render(request,'Cardio/cardio.html')