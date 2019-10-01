from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from heroi.models import Heroi
from heroi.serializers import HeroiSerializer


class HeroiViewSet(viewsets.ModelViewSet):
    filter_backends = [SearchFilter]
    search_fields = ['$nome']
    queryset = Heroi.objects.all()
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    # authentication_classes = (TokenAuthentication,)
    serializer_class = HeroiSerializer


def index(request):
    return render(request, 'index.html')

def detalhe(request, id):
    heroi = Heroi.objects.get(id=id)
    habilidades = heroi.habilidade_heroi.all()
    
    contexto = {
        'heroi': heroi,
        'habilidades': habilidades
    }
    return render(request, 'detalhe.html', contexto)
    

def lista(request):
    herois = Heroi.objects.all()

    contexto = {
        'herois': herois
    }
    return render(request, 'lista.html', contexto)