from django.shortcuts import render
from django.http import HttpResponse
from .models import Eleve

# Create your views here.
def index(request):
    template = 'index.html'

    return render(request, template, {'Eleve': Eleve})