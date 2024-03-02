from django.db import models

# Create your models here.
class Campania(models.Model):
    nombre_campania = models.CharField(max_length=100)
    descripcion_campania = models.CharField(max_length=250)
    
    class Meta:
        verbose_name = 'Campania'
        verbose_name_plural = 'Campañas'
        
        ordering = ['nombre_campania']
        #ordering = [-'nombre_campania']       
    
    def __str__(self):
        return self.nombre_campania

class Headset(models.Model):
    marca_headset = models.CharField(max_length=100)
    
    def __str__(self):
        return 'Headset'

class Mouse(models.Model):  
    marca_mouse = models.CharField(max_length=100)
    
    def __str__(self):
        return 'Mouse'

class Notebook(models.Model):
    nombre_notebook = models.CharField(max_length=100)
    marca_notebook = models.CharField(max_length=100)
    numero_serie_notebook = models.CharField(max_length=100)
    modelo_notebook = models.CharField(max_length=100)
    estado_notebook = models.CharField(max_length=100, null=False)
    
    def __str__(self):
        return f'La notebook - Marca: {self.marca_notebook}, Modelo: {self.modelo_notebook}'
    
class Computadora(models.Model):
    nombre_computadora = models.CharField(max_length=100)
    version_windows = models.CharField(max_length=100)
    estado_computadora_escritorio = models.CharField(max_length=200)
    
    def __str__(self):
        return f'Computadora'
    
class Persona(models.Model):
    nombre_persona = models.CharField(max_length=100)
    apellido_persona = models.CharField(max_length=100)
    cuit_persona = models.CharField(max_length=100, null=True, blank=True)
    email_persona = models.EmailField(null=True, blank=True)
    id_notebook = models.OneToOneField(Notebook, on_delete=models.CASCADE, null=True, blank=True, unique=True)
    id_computadora_escritorio = models.OneToOneField(Computadora, on_delete=models.CASCADE, null=True, blank=True, unique=True)
    id_campania = models.ForeignKey(Campania, on_delete=models.CASCADE, null=False, blank=False, unique=False)
    id_headset = models.ForeignKey(Headset, on_delete=models.CASCADE, null=False, blank=False, unique=False)
    id_headset = models.ForeignKey(Mouse, on_delete=models.CASCADE, null=True, blank=True, unique=False )
    
    class Meta:
        ordering = ['nombre_persona', 'apellido_persona']
    
    def __str__(self):
        return f'{self.nombre_persona}, {self.apellido_persona}'