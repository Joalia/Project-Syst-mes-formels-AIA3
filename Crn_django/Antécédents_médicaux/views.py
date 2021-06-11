from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def ante(request):
    return render(request,'Antécédents_médicaux/antecedents_medicaux.html')
