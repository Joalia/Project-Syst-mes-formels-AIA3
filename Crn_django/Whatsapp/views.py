from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def whats(request):
    return render(request,'Whatsapp/whatsapp.html')