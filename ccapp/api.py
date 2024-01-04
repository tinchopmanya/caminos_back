from .models import Especialidad
from .models import Persona
from .models import Tecnico
from .models import Paciente
from .models import Funcionario
from .models import TutorPaciente
from .models import Pago
from .models import Sesion
from .models import Prestador
from .models import Tratamiento
from .models import Consulta
from .models import RegistroConsulta
from .models import Evaluacion
from .models import InstitucionEducativa

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from rest_framework import viewsets, permissions

from .serializers import EspecialidadSerializer
from .serializers import PersonaSerializer
from .serializers import TecnicoSerializer
from .serializers import PacienteSerializer
from .serializers import FuncionarioSerializer
from .serializers import TutorPacienteSerializer
from .serializers import SesionSerializer
from .serializers import ConsultaSerializer
from .serializers import RegistroConsultaSerializer
from .serializers import TratamientoSerializer
from .serializers import EvaluacionSerializer
from .serializers import PagoSerializer
from .serializers import PrestadorSerializer
from .serializers import InstitucionEducativaSerializer
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate  # Import authenticate function
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
    
    
class EspecialidadViewSet(viewsets.ModelViewSet):
    queryset =  Especialidad.objects.all()
    #permission_classes = [permissions.AllowAny]
    permission_classes = (IsAuthenticated,)
    serializer_class = EspecialidadSerializer

    def perform_create(self, serializer):
        print("hola" )
        print( self.request.user.is_authenticated)
        self.request.data.get("title", None)  # read data from request
        if self.request.user.is_authenticated:
            instance = serializer.save(author=self.request.user)
        else:
            instance = serializer.save()  
            
    def get(self, request, format=None):
        print("dejamos ver" )
        content = {
            'status': 'request was permitted'
        }
        return Response(content)
    
    def list(self, request):
        print("dejamos ver lista" )
        queryset = Especialidad.objects.all()        
        serializer = EspecialidadSerializer(queryset, many=True)
        return Response(serializer.data)

   # def retrieve(self, request, pk=None):
        queryset = Especialidad.objects.all()
        #user = get_object_or_404(queryset, pk=pk)
        #serializer = UserSerializer(user)
     #   return Response(serializer.data

    
      
class InstitucionEducativaViewSet(viewsets.ModelViewSet):
    queryset =  InstitucionEducativa.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = InstitucionEducativaSerializer
    #pagination_class = CustomPagination
    
class PersonaViewSet(viewsets.ModelViewSet):
    queryset =  Persona.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PersonaSerializer
    #pagination_class = CustomPagination   
    
class TecnicoViewSet(viewsets.ModelViewSet):
    queryset =  Tecnico.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TecnicoSerializer
    #pagination_class = CustomPagination   
    
class PacienteViewSet(viewsets.ModelViewSet):
    queryset =  Paciente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PacienteSerializer
    #pagination_class = CustomPagination   
    
class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset =  Funcionario.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = FuncionarioSerializer
    #pagination_class = CustomPagination   
    
class TutorPacienteViewSet(viewsets.ModelViewSet):
    queryset =  TutorPaciente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TutorPacienteSerializer
    #pagination_class = CustomPagination   
    
class PagoViewSet(viewsets.ModelViewSet):
    queryset =  Pago.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PagoSerializer
    #pagination_class = CustomPagination   
    
class PrestadorViewSet(viewsets.ModelViewSet):
    queryset =  Prestador.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PrestadorSerializer
    #pagination_class = CustomPagination   
    
class SesionViewSet(viewsets.ModelViewSet):
    queryset =  Sesion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SesionSerializer  
    #pagination_class = CustomPagination   
    
class ConsultaViewSet(viewsets.ModelViewSet):
    queryset =  Consulta.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ConsultaSerializer   
    #pagination_class = CustomPagination   
    
class RegistroConsultaViewSet(viewsets.ModelViewSet):
    queryset =  RegistroConsulta.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegistroConsultaSerializer  
    #pagination_class = CustomPagination   
    
class TratamientoViewSet(viewsets.ModelViewSet):
    queryset =  Tratamiento.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TratamientoSerializer
    #pagination_class = CustomPagination 
      
class EvaluacionViewSet(viewsets.ModelViewSet):
    queryset =  Evaluacion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EvaluacionSerializer
    






       



        
             
      