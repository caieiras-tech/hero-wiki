from django.shortcuts import render
from rest_framework import serializers, viewsets


# Create your views here.
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from universo.models import Universo
from universo.serializers import UniversoSerializer


class UniversoViewSet(viewsets.ModelViewSet):
    filter_backends = [SearchFilter]
    search_fields = ['$nome']
    queryset = Universo.objects.all()
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    # authentication_classes = (TokenAuthentication,)
    serializer_class = UniversoSerializer