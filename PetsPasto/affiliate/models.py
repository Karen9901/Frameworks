from django.db import models

# Create your models here.

class paises(models.Model):
    id=models.AutoField(primary_key=True)
    codigo=models.CharField(max_length=120, null=False)
    nombre=models.CharField(max_length=120)
    abreviatura=models.CharField(max_length=60)
    estado=models.BooleanField()
    fecha_creacion=models.DateTimeField()
    fecha_modificacion=models.DateTimeField()

class ciudades(models.Model):
    id=models.AutoField(primary_key=True)
    codigo=models.CharField(max_length=120, null=False)
    nombre=models.CharField(max_length=120)
    abreviatura=models.CharField(max_length=60)
    id_pais=models.ForeignKey(paises, on_delete=models.CASCADE)
    estado=models.BooleanField()
    fecha_creacion=models.DateTimeField()
    fecha_modificacion=models.DateTimeField()

class afiliados(models.Model):
    id=models.AutoField(primary_key=True)
    nombres=models.CharField(max_length=160)
    apellidos=models.CharField(max_length=160)
    numero_movil=models.IntegerField()
    direccion=models.CharField(max_length=200)
    email=models.EmailField(unique=True)
    id_ciudad=models.ForeignKey(ciudades, on_delete=models.CASCADE)
    estado=models.BooleanField()
    fecha_creacion=models.DateTimeField()
    fecha_modificacion=models.DateTimeField()        