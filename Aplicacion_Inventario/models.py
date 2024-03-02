from django.db import models

# Create your models here.
class Campania(models.Model):
    nombre_campania = models.CharField(max_length=50)
    descripcion_campania = models.CharField(max_length=250)
    
    class Meta:
        verbose_name = 'Campania'
        verbose_name_plural = 'Campañas'
        
        ordering = ['nombre_campania']
        #ordering = [-'nombre_campania']       
    
    def __str__(self):
        return self.nombre_campania

class Periferico(models.Model):
    marca_teclado = models.CharField(max_length=20)    
    marca_mouse = models.CharField(max_length=20)
    marca_auricular = models.CharField(max_length=20)
    
    def __str__(self):
        return 'Periferico'

class Persona(models.Model):
    nombre_persona = models.CharField(max_length=50)
    apellido_persona = models.CharField(max_length=50)
    cuit_persona = models.CharField(max_length=50)
    email_persona = models.EmailField()
    contraseña_preferida_usuario = models.CharField(max_length=10)
    mouse_asignado = models.BooleanField()
    teclado_asignado = models.BooleanField()
    auricular_asignado = models.BooleanField()
    
    class Meta:
        ordering = ['nombre_persona', 'apellido_persona']
    
    def __str__(self):
        return f'{self.nombre_persona}, {self.apellido_persona}'
    
class Notebook(models.Model):
    nombre_notebook = models.CharField(max_length=20)
    marca_notebook = models.CharField(max_length=20)
    numero_serie_notebook = models.CharField(max_length=20)
    modelo_notebook = models.CharField(max_length=20)
    
    def __str__(self):
        return f'La notebook - Marca: {self.marca_notebook}, Modelo: {self.modelo_notebook}'
    
class Computadora(models.Model):
    nombre_computadora = models.CharField(max_length=50)
    
    def __str__(self):
        return f'Computadora'