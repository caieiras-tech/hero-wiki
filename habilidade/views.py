from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter
# Create your views here.
from habilidade.models import Habilidade
from habilidade.serializers import HabilidadeSerializer


class HabilidadeViewSet(viewsets.ModelViewSet):
    filter_backends = [SearchFilter]
    search_fields = ['$nome']
    queryset = Habilidade.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = HabilidadeSerializer