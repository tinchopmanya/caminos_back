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

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User 
        fields = [ 'username', 'password', 'email']




   

class  EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        paginator = CustomPagination()
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
        
        
class  PrestadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestador
        fields = ('idPrestador','nombrePrestador')
        read_only_fields = ('created_at',)       
        
class  PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = ('idPago','fechaPago','total','paciente')
        read_only_fields = ('created_at',)
 
class  SesionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sesion
        fields = ('idSesion','nroTecnico','diaSemana','horaInicio','horaFin','cantidadPacientes','agrupacion','unicavez')
        read_only_fields = ('created_at',) 


        

      
class  TratamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tratamiento
        fields = ('idTratamiento','idPaciente','idPrestador','idSesion','observaciones')
        read_only_fields = ('created_at',)  
        
class  EvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluacion
        fields = ('idEvaluacion','fechaInicio','horaFin','idPaciente','idSesion','diaSemana','idPrestador','horaConsulta','estado','cantidadConsultas','cantidadConsultasRestantes','observaciones')
        read_only_fields = ('created_at',)  
 
    
    
class  PrestadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tratamiento
        fields = ('idTratamiento','idPaciente','idPrestador','idSesion','observaciones')
        read_only_fields = ('created_at',)  
        
class  ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = ('idConsulta','fecha','hora','idSesion','idEvaluacion','idTratamiento' ,'nroTecnico','idPaciente','asisteAfiliado','asisteTecnico','estado','observaciones','fechaGeneracion')
        read_only_fields = ('created_at',)  
      
class  RegistroConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroConsulta
        fields = ('idRegistroConsulta','idConsulta','fecha','hora','nroTecnico','nroTecnico','idPaciente','idEvaluacion','idTratamiento','observaciones')
        read_only_fields = ('created_at',)  
        
        
        
                                                               


        
          
        
        
        
