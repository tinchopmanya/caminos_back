from rest_framework import routers
from .api import EspecialidadViewSet
from .api import PersonaViewSet
from .api import TecnicoViewSet
from .api import PacienteViewSet
from .api import FuncionarioViewSet
from .api import TutorPacienteViewSet
from .api import InstitucionEducativaViewSet

from .api import SesionViewSet
from .api import ConsultaViewSet
from .api import RegistroConsultaViewSet
from .api import TratamientoViewSet
from .api import EvaluacionViewSet
from .api import PagoViewSet
from .api import PrestadorViewSet
from .api import InstitucionEducativa
from django.urls import path , re_path, include


from django.urls import path

from .views import signup
from .views import login
from .views import test_token

from django.urls import re_path

from . import views

urlpatterns = [
    re_path('signup', views.signup),
    re_path('login', views.login),
    re_path('test_token', views.test_token),
]



router = routers.DefaultRouter()



router.register('api/Especialidad', EspecialidadViewSet , basename= 'Especialidad')
router.register('api/InstitucionEducativa', InstitucionEducativaViewSet , basename= 'InstitucionEducativa')
router.register('api/Persona', PersonaViewSet , basename= 'Persona')
router.register('api/Tecnico', TecnicoViewSet , basename= 'Tecnico')
router.register('api/Paciente', PacienteViewSet , basename= 'Paciente')
router.register('api/Funcionario', FuncionarioViewSet , basename= 'Funcionario')
router.register('api/TutorPaciente', TutorPacienteViewSet , basename= 'TutorPaciente')
router.register('api/Prestador', PrestadorViewSet , basename= 'Prestador')
router.register('api/Pago', PagoViewSet , basename= 'Pago')
router.register('api/Sesion', SesionViewSet , basename= 'Sesion')
router.register('api/Tratamiento', TratamientoViewSet , basename= 'Tratamiento')
router.register('api/Evaluacion', EvaluacionViewSet , basename= 'Evaluacion')
router.register('api/Consulta', ConsultaViewSet , basename= 'Consulta')
router.register('api/Registro', RegistroConsultaViewSet , basename= 'Registro')





        


urlpatterns = router.urls
