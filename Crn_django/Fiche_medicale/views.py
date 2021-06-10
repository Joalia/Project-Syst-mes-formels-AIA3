from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fichem(request):
    return render(request,'Fiche_medicale/fiche_medicale.html')