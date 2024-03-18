from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Campania(models.Model):
    nombre_campania = models.CharField(max_length=100)
    descripcion_campania = models.CharField(max_length=250, null=True, blank="True", default='Sin descripción')
    
    class Meta:
        verbose_name = 'Campania'
        verbose_name_plural = 'Campañas'
        
        ordering = ['nombre_campania']
        #ordering = [-'nombre_campania']       
    
    def __str__(self):
        return self.nombre_campania

class Headset(models.Model):
    marca_headset = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Headset'
        verbose_name_plural = 'Headsets'
        
        ordering = ['marca_headset']

    def __str__(self):
        return f'{self.marca_headset}'

class Mouse(models.Model):  
    marca_mouse = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Mouse'
        verbose_name_plural = 'Mouses'
        
        ordering = ['marca_mouse']
    
    def __str__(self):
        return f'{self.marca_mouse}'

class Notebook(models.Model):
    nombre_notebook = models.CharField(max_length=100)
    marca_notebook = models.CharField(max_length=100)
    numero_serie_notebook = models.CharField(max_length=100)
    modelo_notebook = models.CharField(max_length=100)
    estado_notebook = models.CharField(max_length=100)
    
    def __str__(self):
        return f'Número de Serie: {self.numero_serie_notebook} y Nombre: {self.nombre_notebook}'
    
class Computadora(models.Model):
    nombre_computadora = models.CharField(max_length=100)
    version_windows = models.CharField(max_length=100)
    estado_computadora_escritorio = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.nombre_computadora}'
    
class Persona(models.Model):
    nombre_persona = models.CharField(max_length=100)
    apellido_persona = models.CharField(max_length=100)
    cuit_persona = models.CharField(max_length=100)
    email_persona = models.EmailField()
    id_notebook = models.OneToOneField(Notebook, on_delete=models.CASCADE)
    id_computadora_escritorio = models.OneToOneField(Computadora, on_delete=models.CASCADE, null=True, blank=True)
    id_campania = models.ForeignKey(Campania, on_delete=models.CASCADE, null=True, blank=True)
    id_headset = models.ForeignKey(Headset, on_delete=models.CASCADE, null=True, blank=True)
    id_mouse = models.ForeignKey(Mouse, on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        ordering = ['nombre_persona', 'apellido_persona']
    
    def __str__(self):
        return f'{self.nombre_persona}, {self.apellido_persona}'
    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user} {self.imagen}"