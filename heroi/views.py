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