from pyexpat import model
from rest_framework import routers, serializers, viewsets

# Importacion de modelos

from primerComponente.models import PrimertTabla

class PrimertTablaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimertTabla
        fields = ('nombre', 'edad')