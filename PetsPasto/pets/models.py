from django.db import models

# Create your models here.
class tipos(models.Model):
    id=models.AutoField(primary_key=True)
    codigo=models.CharField(max_length=60, null=False)
    nombre=models.CharField(max_length=120 , null=False)
    abreviatura=models.CharField(max_length=50)
    estado=models.BooleanField()
    fecha_creacion=models.DateTimeField()
    fecha_modificacion=models.DateTimeField()

class razas(models.Model):
    id=models.AutoField(primary_key=True)
    codigo=models.CharField(max_length=60, null=False)
    nombre=models.CharField(max_length=120 , null=False)
    abreviatura=models.CharField(max_length=50)
    id_tipo=models.ForeignKey(tipos, on_delete=models.CASCADE)
    estado=models.BooleanField()
    fecha_creacion=models.DateTimeField()
    fecha_modificacion=models.DateTimeField()

class mascotas(models.Model):
    id=models.AutoField(primary_key=True)
    codigo=models.CharField(max_length=60, null=False)
    id_tipo=models.ForeignKey(tipos, on_delete=models.CASCADE)
    id_raza=models.ForeignKey(razas, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=120)
    tiene_vacunas=models.BooleanField()
    estado=models.BooleanField()
    fecha_creacion=models.DateTimeField()
    fecha_modificacion=models.DateTimeField()    