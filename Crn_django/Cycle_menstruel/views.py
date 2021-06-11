from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def cycle(request):
    return render(request,'Cycle_menstruel/cycle_menstruel.html')