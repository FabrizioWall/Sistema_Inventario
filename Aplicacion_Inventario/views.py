from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.
# ------------------------------------ Página Principal ---------------------------------------------
def index(request):
    current_user = request.user
    return render(request, 'Aplicacion_Inventario/index.html', {'current_user': current_user})

# ------------------------------------ Login ---------------------------------------------
def login_request(request):
    if request.method == 'POST':
        usuario = request.POST['username']
        clave = request.POST['password']
        user = authenticate(request, username=usuario, password=clave)
        
        if not User.objects.filter(username=usuario).exists():
            messages.error(request, "El usuario no éxiste en la base de datos. Regístrese.")
            return redirect(reverse_lazy('login_sistema'))
        elif user is not None:
            login(request, user)
            return redirect(reverse_lazy('index'))
        else:
            messages.error(request, "Contraseña incorrecta.")
            return redirect(reverse_lazy('login_sistema'))
        
    else:
        miFormLogin = AuthenticationForm()

    return render(request, 'Aplicacion_Inventario/login.html', {'form': miFormLogin})

# ------------------------------------ Registro ---------------------------------------------
def registro_request(request):
    if request.method == 'POST':
        miFormRegistro = RegistroForm(request.POST)
        
        if miFormRegistro.is_valid():
            usuario = miFormRegistro.cleaned_data.get('username')
            miFormRegistro.save()
            return redirect(reverse_lazy('login_sistema'))
        else:
            messages.error(request, "ERROR: Las contraseñas deben coincidir.")
            return redirect(reverse_lazy('registro_sistema'))
        
    else:
        miFormRegistro = RegistroForm()
        
    return render(request, 'Aplicacion_Inventario/registro.html', {'form': miFormRegistro})


# ------------------------------------ Notebooks ---------------------------------------------

#CRUD: 'Crear' y 'Buscar (read) están definidas en esta función!
def notebooks(request):
    # -------------------------- Create --------------------------------
    if request.method == 'POST':
        miFormularioNotebook = NotebookForm(request.POST)
        
        if miFormularioNotebook.is_valid():
            miFormularioNotebook.save()
            return redirect(reverse_lazy('notebooks'))
        
    else:
        miFormularioNotebook = NotebookForm()
    
    # -------------------------- Read --------------------------------
    buscar_notebook = request.GET.get('buscar_notebook')
    if buscar_notebook:
        notebook = Notebook.objects.filter(nombre_notebook__icontains=buscar_notebook)
        contexto = {
                    'notebooks': notebook, 
                    'miFormularioNotebook': miFormularioNotebook, 
                    'current_user': request.user}
    else:
        contexto = {
                    'notebooks': Notebook.objects.all().order_by('id'), 
                    'miFormularioNotebook': miFormularioNotebook, 
                    'current_user': request.user}
    
    return render(request, 'Aplicacion_Inventario/notebooks.html', contexto)

class NotebookUpdate(UpdateView): #CRUD: Update
    model = Notebook
    fields = ['nombre_notebook', 'nombre_notebook', 'marca_notebook', 'numero_serie_notebook', 
                  'modelo_notebook', 'estado_notebook']
    success_url = reverse_lazy('notebooks')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_user'] = self.request.user
        return context

class NotebookDelete(DeleteView): #CRUD: Delete
    model = Notebook
    success_url = reverse_lazy('notebooks')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_user'] = self.request.user
        return context


# ------------------------------------ Campañas ---------------------------------------------

#CRUD: 'Crear' y 'Buscar (read) están definidas en esta función!
def campanias(request):
    # -------------------------- Create --------------------------------
    if request.method == 'POST':
        miFormularioCampania = CampaniaForm(request.POST)
        
        if miFormularioCampania.is_valid():
            miFormularioCampania.save()
            return redirect(reverse_lazy('campanias'))
    
    else:
        miFormularioCampania = CampaniaForm()
    
    # -------------------------- Read --------------------------------
    buscar_campania = request.GET.get('buscar_campania')
    if buscar_campania:
        campania = Campania.objects.filter(nombre_campania__icontains=buscar_campania)
        contexto = {
                    'campanias': campania, 
                    'miFormularioCampania': miFormularioCampania, 
                    'current_user': request.user}
    else:
        contexto = {
                    'campanias': Campania.objects.all().order_by('id'), 
                    'miFormularioCampania': miFormularioCampania, 
                    'current_user': request.user}
    
    
    return render(request, 'Aplicacion_Inventario/campanias.html', contexto)

class CampaniaUpdate(UpdateView): #CRUD: Update
    model = Campania
    fields = ['nombre_campania', 'descripcion_campania']
    success_url = reverse_lazy('campanias')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_user'] = self.request.user
        return context
    
class CampaniaDelete(DeleteView): #CRUD: Delete
    model = Campania
    success_url = reverse_lazy('campanias')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_user'] = self.request.user
        return context


# ------------------------------------ PC's ---------------------------------------------

#CRUD: 'Crear' y 'Buscar (read) están definidas en esta función!
def computadoras_escritorio(request):
    # -------------------------- Create --------------------------------
    if request.method == 'POST':
        miFormularioComputadora = ComputadoraForm(request.POST)
        
        if miFormularioComputadora.is_valid():
            miFormularioComputadora.save()
            return redirect(reverse_lazy('computadoras'))
    
    else:
        miFormularioComputadora = ComputadoraForm()
        
    # -------------------------- Read --------------------------------
    buscar_computadora = request.GET.get('buscar_computadora')
    if buscar_computadora:
        computadora = Computadora.objects.filter(nombre_computadora__icontains=buscar_computadora)
        contexto = {
                    'computadoras': computadora, 
                    'miFormularioComputadora': miFormularioComputadora, 
                    'current_user': request.user}
    else:
        contexto = {
                    'computadoras': Computadora.objects.all().order_by('id'), 
                    'miFormularioComputadora': miFormularioComputadora, 
                    'current_user': request.user}
    
    
    return render(request, 'Aplicacion_Inventario/computadoras_escritorio.html', contexto)

class ComputadoraUpdate(UpdateView): #CRUD: Update
    model = Computadora
    fields = ['nombre_computadora', 'version_windows', 'estado_computadora_escritorio']
    success_url = reverse_lazy('computadoras')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_user'] = self.request.user
        return context
    
class ComputadoraDelete(DeleteView): #CRUD: Delete
    model = Computadora
    success_url = reverse_lazy('computadoras')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_user'] = self.request.user
        return context

# ------------------------------------ Perifericos ---------------------------------------------

#CRUD: 'Crear' y 'Buscar (read) están definidas en esta función!
def perifericos(request):
    # -------------------------- Create: MOUSE --------------------------------
    if request.method == 'POST':
        miFormularioMouse = MouseForm(request.POST)
        
        if miFormularioMouse.is_valid():
            miFormularioMouse.save()
            return redirect(reverse_lazy('perifericos'))
    
    else:
        miFormularioMouse = MouseForm()
    
    # -------------------------- Read: MOUSE --------------------------------
    buscar_mouse = request.GET.get('buscar_mouse')
    if buscar_mouse:
        mouses = Mouse.objects.filter(marca_mouse__icontains=buscar_mouse)
    else:
        mouses = Mouse.objects.all().order_by('id')

    # -------------------------- Create: HEADSET --------------------------------
    if request.method == 'POST':
        miFormularioHeadset = HeadsetForm(request.POST)
        
        if miFormularioHeadset.is_valid():
            miFormularioHeadset.save()
            (reverse_lazy('perifericos'))
    
    else:
        miFormularioHeadset = HeadsetForm()
        
    # -------------------------- Read: HEADSET --------------------------------
    buscar_headset = request.GET.get('buscar_headset')
    if buscar_headset:
        headsets = Headset.objects.filter(marca_headset__icontains=buscar_headset)
    else:
        headsets = Headset.objects.all().order_by('id')

    contexto = {
        'mouses': mouses,
        'miFormularioMouse': miFormularioMouse,
        'headsets': headsets,
        'miFormularioHeadset': miFormularioHeadset,
        'current_user': request.user
    }
    
    return render(request, 'Aplicacion_Inventario/perifericos.html', contexto)

# ----- Mouse ---------------------------------------------
class MouseUpdate(UpdateView): #CRUD: Update
    model = Mouse
    fields = ['marca_mouse']
    success_url = reverse_lazy('perifericos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_user'] = self.request.user
        return context
    
class MouseDelete(DeleteView): #CRUD: Delete
    model = Mouse
    success_url = reverse_lazy('perifericos')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_user'] = self.request.user
        return context

# ----- Headset ---------------------------------------------
class HeadsetUpdate(UpdateView): #CRUD: Update
    model = Headset
    fields = ['marca_headset']
    success_url = reverse_lazy('perifericos')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_user'] = self.request.user
        return context
    
class HeadsetDelete(DeleteView): #CRUD: Delete
    model = Headset
    success_url = reverse_lazy('perifericos')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_user'] = self.request.user
        return context


# ------------------------------------ Personas ---------------------------------------------

#CRUD: 'Crear' y 'Buscar (read) están definidas en esta función!
def personas(request):
    # -------------------------- Create --------------------------------
    if request.method == 'POST':
        miFormularioPersona = PersonaForm(request.POST)
        if miFormularioPersona.is_valid():
            miFormularioPersona.save()
            return redirect(reverse_lazy('personas'))
    else:
        miFormularioPersona = PersonaForm()

    # -------------------------- Read --------------------------------
    buscar_persona = request.GET.get('buscar_persona')
    if buscar_persona:
        personas = Persona.objects.filter(nombre_persona__icontains=buscar_persona)
    else:
        personas = Persona.objects.all().order_by('id')

    contexto = {
        'personas': personas,
        'campanias': Campania.objects.all(),
        'notebooks': Notebook.objects.all(),
        'headsets': Headset.objects.all(),
        'mouses': Mouse.objects.all(),
        'computadoras': Computadora.objects.all(),
        'miFormularioPersona': miFormularioPersona,
        'current_user': request.user
    }
    
    return render(request, 'Aplicacion_Inventario/personas.html', contexto)

class PersonaUpdate(UpdateView): #CRUD: Update
    model = Persona
    fields = ['nombre_persona', 'apellido_persona', 'cuit_persona', 'email_persona', 
                'id_notebook', 'id_computadora_escritorio', 
                'id_campania', 'id_headset', 'id_mouse']
    success_url = reverse_lazy('personas')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_user'] = self.request.user
        return context
    
class PersonaDelete(DeleteView): #CRUD: Delete
    model = Persona
    success_url = reverse_lazy('personas')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_user'] = self.request.user
        return context




