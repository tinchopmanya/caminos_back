from .models import Especalidad
from rest_framework import viewsets, permissions
from .serializers import EspecialidadSerializer

class EspecialidadViewSet(viewsets.ModelViewSet):
    queryset =  Especalidad.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EspecialidadSerializer