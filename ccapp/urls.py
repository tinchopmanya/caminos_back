from rest_framework import routers
from .api import EspecialidadViewSet
from .api import UsuarioViewSet
from .api import PersonaViewSet
from .api import TecnicoViewSet
from .api import PacienteViewSet
from .api import FuncionarioViewSet
from .api import TutorPacienteViewSet

router = routers.DefaultRouter()

router.register('api/Especialidad', EspecialidadViewSet , basename= 'Especialidad')
router.register('api/Usuario', UsuarioViewSet , basename= 'Usuario')
router.register('api/Persona', PersonaViewSet , basename= 'Persona')
router.register('api/Tecnico', TecnicoViewSet , basename= 'Tecnico')
router.register('api/Paciente', PacienteViewSet , basename= 'Paciente')
router.register('api/Funcionario', FuncionarioViewSet , basename= 'Funcionario')
router.register('api/TutorPaciente', TutorPacienteViewSet , basename= 'TutorPaciente')




urlpatterns = router.urls
