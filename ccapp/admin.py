from django.contrib import admin
from rest_framework.authtoken.models import Token
from .models import Especialidad
from .models import InstitucionEducativa
from .models import Persona
from .models import Tecnico
from .models import Prestador
from .models import Paciente
from .models import Funcionario
from .models import TutorPaciente
from .models import Pago
from .models import Sesion
from .models import Tratamiento
from .models import Evaluacion
from .models import Consulta

admin.site.register(Especialidad)
admin.site.register(InstitucionEducativa)
admin.site.register(Persona)
admin.site.register(Tecnico)
admin.site.register(Prestador)
admin.site.register(Paciente)
admin.site.register(Funcionario)
admin.site.register(TutorPaciente)
admin.site.register(Pago)
admin.site.register(Sesion)
admin.site.register(Tratamiento)
admin.site.register(Evaluacion)
admin.site.register(Consulta)

# Register your models here.
