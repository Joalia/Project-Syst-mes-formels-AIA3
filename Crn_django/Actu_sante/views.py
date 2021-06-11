from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def actu(request):
    return render(request,'Actu_sante/actu_sante.html')