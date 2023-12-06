from rest_framework import serializers  

from .models import Especalidad

class  EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especalidad
        fields = ('idEspecialidad','nombreEspecialidad','fechacreado')
        read_only_fields = ('fechacreado',)