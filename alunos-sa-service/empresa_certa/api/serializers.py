from rest_framework.serializers import ModelSerializer
from empresa_certa.models import EmpresaCerta


class EmpresaCertaSerializer(ModelSerializer):
    class Meta:
        model = EmpresaCerta
        fields = '__all__'
