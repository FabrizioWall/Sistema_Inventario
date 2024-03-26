from .models import *

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)
    
class UserEditForm(UserChangeForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label="Nombre/s", max_length=100, required=True)
    last_name = forms.CharField(label="Apellido/s", max_length=100, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        
class RegistroForm(UserCreationForm):
    nombre = forms.CharField(required=True)
    apellido = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'nombre', 'apellido', 'email', 'password1', 'password2' ]

# ---------------------------- Form Modelos ---------------------------------------------
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
    
    def __init__(self, *args, **kwargs):
        super(PersonaForm, self).__init__(*args, **kwargs)
        # Se filtra las opciones de la lista desplegable para id_notebook
        self.fields['id_notebook'].queryset = Notebook.objects.filter(persona__isnull=True)
    
    class Meta:
        model = Persona
        fields = ['nombre_persona', 'apellido_persona', 'cuit_persona', 'email_persona', 
                  'id_notebook', 'id_computadora_escritorio', 
                  'id_campania', 'id_headset', 'id_mouse']