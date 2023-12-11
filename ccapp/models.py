from django.db import models

# Create your models here.
    
class Usuario(models.Model):
    usuario = models.CharField(max_length=10)
    password = models.CharField(max_length=160)  
    created_at = models.DateTimeField(auto_now_add=True)  
    
class Especialidad(models.Model):
    idEspecialidad = models.AutoField(primary_key=True)
    nombreEspecialidad = models.TextField()
    estadoEspecialidad = models.SmallIntegerField()
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
    usuario = models.ForeignKey(Usuario , on_delete = models.CASCADE)
    Persona = models.ForeignKey(Persona , on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
     
class Paciente(models.Model):
    idPaciente = models.IntegerField()
    nroCJPPU = models.CharField(max_length=12) 
    fechaVencimientoAYEX = models.DateField()
    esBPS = models.CharField(max_length=1) 
    deuda = models.IntegerField()
    Persona = models.ForeignKey(Persona , on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Funcionario(models.Model):
    nroFuncionario = models.IntegerField()
    usuario = models.ForeignKey(Usuario , on_delete = models.CASCADE)
    Persona = models.ForeignKey(Persona , on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
class TutorPaciente(models.Model):
    Persona = models.ForeignKey(Persona , on_delete = models.CASCADE)
    pacientes = models.ManyToManyField(Paciente)
    created_at = models.DateTimeField(auto_now_add=True)   

 