from rest_framework import serializers  
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from rest_framework.pagination import PageNumberPagination


from .models import Persona
from .models import Especialidad
from .models import Tecnico
from .models import Paciente
from .models import TutorPaciente
from .models import Funcionario
from .models import Pago
from .models import Sesion
from .models import Prestador
from .models import Tratamiento
from .models import Consulta
from .models import RegistroConsulta
from .models import Evaluacion
from .models import InstitucionEducativa


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10
    

#Serializer to Get User Details using Django Token Authentication
#class UserSerializer(serializers.ModelSerializer):
#  class Meta:
#    model = User
#    fields = ["id", "first_name", "last_name", "username"]
    

from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.models import Group


    
    
class UserSerializer(serializers.ModelSerializer):
    group = serializers.SerializerMethodField()
      
    class Meta(object):
        model = User 
        fields = [ 'username', 'password', 'email', 'group']

    def get_group(self, obj):
        group = Group.objects.filter(user=obj).first()
        return group.name if group else None


 

class  EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        paginator = CustomPagination()
        fields = ('idEspecialidad','nombreEspecialidad','activo')
        extra_kwargs = {
            "author": {"required": False, "allow_null": True}
        }
        read_only_fields = ('created_at',)   
 
 
class  InstitucionEducativaSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstitucionEducativa
        paginator = CustomPagination()
        fields = ('idInstitucionEducativa','nombreInstitucionEducativa','activo')
        extra_kwargs = {
            "author": {"required": False, "allow_null": True}
        }
        read_only_fields = ('created_at',) 
               

               
class  PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Persona
        fields = ('cedula','digito','primernombre','primerapellido','segundonombre','segundoapellido','email','celular','direccion','ciudad','localidad','fechaNacimiento','imagen','activo')
        extra_kwargs = {
            "author": {"required": False, "allow_null": True}
        }
        read_only_fields = ('created_at',)
        
        
class  TecnicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnico
        fields = ('nroTecnico','nroCJPPU','especialidades','usuario','persona','activo')
        extra_kwargs = {
            "author": {"required": False, "allow_null": True}
        }
        read_only_fields = ('created_at',)
        
class  PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ('idPaciente','fechaVencimientoAYEX','esBPS','deuda','persona','activo')
        extra_kwargs = {
            "author": {"required": False, "allow_null": True}
        }
        read_only_fields = ('created_at',)
        
class  TutorPacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutorPaciente
        fields = ('persona','pacientes','activo')
        extra_kwargs = {
            "author": {"required": False, "allow_null": True}
        }
        read_only_fields = ('created_at',)
        
        
class  FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ('nroFuncionario','usuario','persona','activo')
        extra_kwargs = {
            "author": {"required": False, "allow_null": True}
        }
        read_only_fields = ('created_at',)
        
        
class  PrestadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestador
        fields = ('idPrestador','nombrePrestador','activo')
        extra_kwargs = {
            "author": {"required": False, "allow_null": True}
        }
        read_only_fields = ('created_at',)       
        
class  PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = ('idPago','fechaPago','total','paciente','activo')
        extra_kwargs = {
            "author": {"required": False, "allow_null": True}
        }
        read_only_fields = ('created_at',)
 
class  SesionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sesion
        fields = ('idSesion','nroTecnico', 'idEspecialidad' , 'diaSemana','horaInicio','horaFin','cantidadPacientes','agrupacion','unicavez','activo')
        extra_kwargs = {
            "author": {"required": False, "allow_null": True}
        }
        read_only_fields = ('created_at',)         

      
class  TratamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tratamiento
        fields = ('idTratamiento','idPaciente','idPrestador','idSesion','observaciones','activo')
        extra_kwargs = {
            "author": {"required": False, "allow_null": True}
        }
        read_only_fields = ('created_at',)  
        
class  EvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluacion
        fields = ('idEvaluacion','fechaInicio','horaFin','idPaciente','idSesion','diaSemana','idPrestador','horaConsulta','estado','cantidadConsultas','cantidadConsultasRestantes','observaciones','activo')
        extra_kwargs = {
            "author": {"required": False, "allow_null": True}
        }
        read_only_fields = ('created_at',)  
 
    
    
class  PrestadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tratamiento
        fields = ('idTratamiento','idPaciente','idPrestador','idSesion','observaciones','activo')
        extra_kwargs = {
            "author": {"required": False, "allow_null": True}
        }
        read_only_fields = ('created_at',)  
        
class  ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = ('idConsulta','fecha','hora','idSesion','idEvaluacion','idTratamiento' ,'nroTecnico','idPaciente','asisteAfiliado','asisteTecnico','estado','observaciones','fechaGeneracion','activo')
        extra_kwargs = {
            "author": {"required": False, "allow_null": True}
        }
        read_only_fields = ('created_at',)  
      
class  RegistroConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroConsulta
        fields = ('idRegistroConsulta','idConsulta','fecha','hora','nroTecnico','nroTecnico','idPaciente','idEvaluacion','idTratamiento','observaciones','activo')
        extra_kwargs = {
            "author": {"required": False, "allow_null": True}
        }
        read_only_fields = ('created_at',)  
        
        
        
                                                               


        
          
        
        
        
