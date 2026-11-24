from rest_framework import serializers
from .models import Lote

class LoteSerializer(serializers.ModelSerializer):
    total = serializers.ReadOnlyField()

    class Meta:
        model = Lote
        fields = ["id", "variedade", "caixas", "preco_caixa", "data", "produtor", "total"]