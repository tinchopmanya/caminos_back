from rest_framework import serializers  
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

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

#Serializer to Get User Details using Django Token Authentication
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ["id", "first_name", "last_name", "username"]

#Serializer to Register User
class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())]
  )
  password = serializers.CharField(
    write_only=True, required=True, validators=[validate_password])
  password2 = serializers.CharField(write_only=True, required=True)
  class Meta:
    model = User
    fields = ('username', 'password', 'password2',
         'email', 'first_name', 'last_name')
    extra_kwargs = {
      'first_name': {'required': True},
      'last_name': {'required': True}
    }
  def validate(self, attrs):
    if attrs['password'] != attrs['password2']:
      raise serializers.ValidationError(
        {"password": "Password fields didn't match."})
    return attrs
  def create(self, validated_data):
    user = User.objects.create(
      username=validated_data['username'],
      email=validated_data['email'],
      first_name=validated_data['first_name'],
      last_name=validated_data['last_name']
    )
    user.set_password(validated_data['password'])
    user.save()
    return user

   

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
        
        
class  PrestadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestador
        fields = ('idPrestador','nombrePrestador')
        read_only_fields = ('created_at',)       
        
class  PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = ('idPago','fechaPago','total')
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
        fields = ('idConsulta','fecha','hora','idSesion','idEvaluacion','idTratamiento' ,'nroTecnico','idPaciente','asisteAfiliado','asisteTecnico','estado','cantidadConsultas','cantidadConsultasRestantes','observaciones','fechaGeneracion')
        read_only_fields = ('created_at',)  
      
class  RegistroConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroConsulta
        fields = ('idRegistroConsulta','idConsulta','fecha','hora','nroTecnico','nroTecnico','idPaciente','idEvaluacion','idTratamiento','observaciones')
        read_only_fields = ('created_at',)  
        
        
        
                                                               


        
          
        
        
        
