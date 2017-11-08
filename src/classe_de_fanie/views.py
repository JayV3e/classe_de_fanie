from django.shortcuts import render
from django.http import HttpResponse
from .models import Eleve

#from lockdown.decorators import lockdown

# Create your views here.
#@lockdown()
def index(request):
    template = 'index.html'
    eleves = Eleve.objects.order_by('non_enseignant','prenom_eleve')


    return render(request, template, {'eleves': eleves})