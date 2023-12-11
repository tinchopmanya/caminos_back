from .models import Especialidad
from .models import Persona
from .models import Tecnico
from .models import Paciente
from .models import Funcionario
from .models import TutorPaciente

from rest_framework import viewsets, permissions

from .serializers import EspecialidadSerializer
from .serializers import PersonaSerializer
from .serializers import TecnicoSerializer
from .serializers import PacienteSerializer
from .serializers import FuncionarioSerializer
from .serializers import TutorPacienteSerializer

class EspecialidadViewSet(viewsets.ModelViewSet):
    queryset =  Especialidad.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EspecialidadSerializer
    
    
class PersonaViewSet(viewsets.ModelViewSet):
    queryset =  Persona.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PersonaSerializer
    
class TecnicoViewSet(viewsets.ModelViewSet):
    queryset =  Tecnico.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TecnicoSerializer
    
class PacienteViewSet(viewsets.ModelViewSet):
    queryset =  Paciente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PacienteSerializer
    
class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset =  Funcionario.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = FuncionarioSerializer
    
class TutorPacienteViewSet(viewsets.ModelViewSet):
    queryset =  TutorPaciente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TutorPacienteSerializer