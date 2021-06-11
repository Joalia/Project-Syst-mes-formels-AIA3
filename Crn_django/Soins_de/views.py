from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def soins(request):
    return render(request,'Soins_de/soins_de.html')