from django.db import models
from django.conf import settings
# Create your models here.
    
    
class Especialidad(models.Model):
    idEspecialidad = models.AutoField(primary_key=True)
    nombreEspecialidad = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    #tecnicos = models.ManyToManyField(Tecnico)
    
class Persona(models.Model):
    cedula = models.CharField(max_length=20 ,primary_key=True)
    digito = models.CharField(max_length=1)
    primernombre = models.CharField(max_length=50)
    primerapellido = models.CharField(max_length=50)
    segundonombre = models.CharField(max_length=50)
    segundoapellido = models.CharField(max_length=50)  
    email = models.CharField(max_length=50)    
    celular = models.CharField(max_length=12)    
    direccion = models.CharField(max_length=80) 
    ciudad = models.CharField(max_length=50)    
    localidad = models.CharField(max_length=50)    
    fechaNacimiento = models.DateField()
    imagen = models.CharField(max_length=100, default='', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Tecnico(models.Model):
    nroTecnico = models.AutoField(primary_key=True)
    nroCJPPU = models.CharField(max_length=12) 
    especialidades = models.ManyToManyField(Especialidad)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete = models.CASCADE)
    persona = models.ForeignKey(Persona , on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
     
class Paciente(models.Model):
    idPaciente = models.AutoField(primary_key=True)
    nroCJPPU = models.CharField(max_length=12) 
    fechaVencimientoAYEX = models.DateField()
    esBPS = models.CharField(max_length=1) 
    deuda = models.IntegerField()
    persona = models.ForeignKey(Persona , on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Funcionario(models.Model):
    nroFuncionario = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete = models.CASCADE)
    persona = models.ForeignKey(Persona , on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
class TutorPaciente(models.Model):
    persona = models.ForeignKey(Persona , on_delete = models.CASCADE)
    pacientes = models.ManyToManyField(Paciente)
    created_at = models.DateTimeField(auto_now_add=True)   

class Pago(models.Model):
    idPago = models.AutoField(primary_key=True)
    fechaPago = models.DateTimeField()
    total = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
     
class Sesion(models.Model):
    idSesion = models.AutoField(primary_key=True)
    nroTecnico = models.ForeignKey(Tecnico , on_delete = models.PROTECT)
    diaSemana = models.IntegerField()
    horaInicio = models.DateTimeField()
    horaFin = models.DateTimeField()
    cantidadPacientes = models.IntegerField()
    agrupacion = models.IntegerField()
    unicavez = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

class Prestador(models.Model):
    idPrestador = models.AutoField(primary_key=True)
    nombrePrestador = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Tratamiento(models.Model):
    idTratamiento = models.AutoField(primary_key=True)
    idPaciente = models.ForeignKey(Paciente , on_delete = models.PROTECT)
    idPrestador = models.ForeignKey(Prestador , on_delete = models.PROTECT)
    idSesion = models.ForeignKey(Sesion , on_delete = models.PROTECT)
    observaciones = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

class Evaluacion(models.Model):
    idEvaluacion = models.AutoField(primary_key=True)
    fechaInicio = models.DateTimeField()
    horaFin = models.DateTimeField()
    idPaciente = models.ForeignKey(Paciente , on_delete = models.PROTECT)
    idSesion = models.ForeignKey(Sesion , on_delete = models.PROTECT)
    diaSemana = models.IntegerField()
    idPrestador = models.ForeignKey(Prestador , on_delete = models.PROTECT)
    horaConsulta = models.DateTimeField() 
    estado = models.IntegerField()
    cantidadConsultas = models.IntegerField()
    cantidadConsultasRestantes = models.IntegerField()
    observaciones = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

class Consulta(models.Model):
    idConsulta = models.AutoField(primary_key=True)
    fecha = models.DateTimeField()
    hora = models.DateTimeField() 
    idSesion = models.ForeignKey(Sesion , on_delete = models.PROTECT)
    idEvaluacion =models.ForeignKey(Evaluacion , on_delete = models.PROTECT)
    idTratamiento = models.ForeignKey(Tratamiento , on_delete = models.PROTECT)
    nroTecnico = models.ForeignKey(Tecnico , on_delete = models.PROTECT)
    idPaciente = models.ForeignKey(Paciente , on_delete = models.PROTECT)
    asisteAfiliado = models.BooleanField()
    asisteTecnico = models.BooleanField()
    estado = models.IntegerField()
    cantidadConsultas = models.IntegerField()
    cantidadConsultasRestantes = models.IntegerField()
    observaciones = models.CharField(max_length=250)
    fechaGeneracion = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    
class RegistroConsulta(models.Model):
    idRegistroConsulta = models.AutoField(primary_key=True)
    idConsulta = models.ForeignKey(Consulta , on_delete = models.PROTECT)
    fecha = models.DateTimeField()
    hora = models.DateTimeField() 
    nroTecnico = models.ForeignKey(Tecnico , on_delete = models.PROTECT)
    idPaciente = models.ForeignKey(Paciente , on_delete = models.PROTECT)
    idEvaluacion =models.ForeignKey(Evaluacion , on_delete = models.PROTECT)
    idTratamiento = models.ForeignKey(Tratamiento , on_delete = models.PROTECT)
    observaciones = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)