from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Importaciones de modelos
from primerComponente.models import PrimertTabla

# Importaciones de serializadores
from primerComponente.serializers import PrimertTablaSerializer

# Create your views here.
class PrimertTablaList(APIView):
    def get(self, request, format=None):
      queryset = PrimertTabla.objects.all()
      serializer = PrimertTablaSerializer(queryset, many = True ,context = {'request':request})
      return Response(serializer.data)