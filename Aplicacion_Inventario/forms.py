from django import forms
from .models import *

class NotebookForm(forms.ModelForm):
    class Meta:
        model = Notebook
        fields = ['nombre_notebook', 'marca_notebook', 'numero_serie_notebook', 
                  'modelo_notebook', 'estado_notebook']

class CampaniaForm(forms.ModelForm):
    class Meta:
        model = Campania
        fields = ['nombre_campania', 'descripcion_campania']
        
class ComputadoraForm(forms.ModelForm):
    class Meta:
        model = Computadora
        fields = ['nombre_computadora', 'version_windows', 'estado_computadora_escritorio']
        
class MouseForm(forms.ModelForm):
    class Meta:
        model = Mouse
        fields = ['marca_mouse']

class HeadsetForm(forms.ModelForm):
    class Meta:
        model = Headset
        fields = ['marca_headset']

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre_persona', 'apellido_persona', 'cuit_persona', 'email_persona', 
                  'id_notebook', 'id_computadora_escritorio', 
                  'id_campania', 'id_headset', 'id_mouse']