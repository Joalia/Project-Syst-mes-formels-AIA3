from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def consul(request):
    return render(request,'Consultations/consultations.html')
