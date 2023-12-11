from rest_framework import serializers  

from .models import Persona
from .models import Especialidad
from .models import Tecnico
from .models import Paciente
from .models import TutorPaciente
from .models import Funcionario


class  EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = ('idEspecialidad','nombreEspecialidad')
        read_only_fields = ('created_at',)   
        


    
       
       
class  PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Persona
        fields = ('cedula','digito','primernombre','primerapellido','segundonombre','segundoapellido','email','celular','direccion','ciudad','localidad','fechaNacimiento','imagen')
        read_only_fields = ('created_at',)
        
        
class  TecnicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnico
        fields = ('nroTecnico','nroCJPPU','especialidades','usuario','persona')
        read_only_fields = ('created_at',)
        
class  PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ('idPaciente','fechaVencimientoAYEX','esBPS','deuda','persona')
        read_only_fields = ('created_at',)
        
class  TutorPacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutorPaciente
        fields = ('persona','pacientes')
        read_only_fields = ('created_at',)
        
        
class  FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ('nroFuncionario','usuario','persona')
        read_only_fields = ('created_at',)
        
        
        
