from django.shortcuts import render
from django.http import HttpResponse
from .models import Eleve

# Create your views here.
def index(request):
    template = 'index.html'
    eleves = Eleve.objects.filter(prenom_eleve = "Clara")

    return render(request, template, {'eleves': eleves})