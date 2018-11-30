from rest_framework.serializers import ModelSerializer

from banco.models import Conta


class BancoSerializer(ModelSerializer):
    class Meta:
        model = Conta
        fields = '__all__'
