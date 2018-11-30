from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from banco.api.serializers import BancoSerializer
from banco.models import Conta


class BancoViewSet(ModelViewSet):
    serializer_class = BancoSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('numero',)

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        numero = self.request.query_params.get('numero', None)
        queryset = Conta.objects.all()

        if id:
            queryset = Conta.objects.filter(pk=id)

        if numero:
            queryset = queryset.filter(numero=numero)

        return queryset
