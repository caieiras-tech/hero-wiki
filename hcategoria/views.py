from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from hcategoria.models import Categoria
from hcategoria.serializers import CategoriaSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    filter_backends = [SearchFilter]
    search_fields = ['$nome']
    queryset = Categoria.objects.all()
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    # authentication_classes = (TokenAuthentication,)
    serializer_class = CategoriaSerializer