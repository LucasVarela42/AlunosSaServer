from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from empresa_certa.api.serializers import EmpresaCertaSerializer
from empresa_certa.models import EmpresaCerta


class EmpresaCertaViewSet(ModelViewSet):
    serializer_class = EmpresaCertaSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('nome',)

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        queryset = EmpresaCerta.objects.all()

        if id:
            queryset = EmpresaCerta.objects.filter(pk=id)

        if nome:
            queryset = queryset.filter(nome__iexact=nome)

        return queryset
