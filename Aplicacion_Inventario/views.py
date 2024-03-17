from django.views.generic import UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import login, authenticate
from django.contrib import messages

from .models import *
from .forms import *

from datetime import datetime
current_date = datetime.now().date() 
import csv

# Create your views here.
# ------------------------------------ Experimental ---------------------------------------------
# Exportar
def exportar(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="datos.csv"'

    personas = Persona.objects.all()  # Obtén todas las personas (o puedes filtrar según tus necesidades)

    writer = csv.writer(response)
    writer.writerow(['Identificador', 'Nombre', 'Notebook', 'Campaña asignada'])  # Encabezados de columna

    for persona in personas:
        writer.writerow([persona.id, persona.nombre_persona + ' ' + persona.apellido_persona, persona.id_notebook, persona.id_campania])

    return response


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
            
            #______________Avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = '/media/avatares/default.png'
            finally:
                request.session['avatar'] = avatar
            
            
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


# ------------------------------------ Edición de perfil ---------------------------------------------
@login_required
def profile(request):
    usuario = request.user
    print("Valor de usuario:", usuario)
    
    if request.method == 'POST':
        print("Datos POST:", request.POST)
        
        formEdit = UserEditForm(request.POST)
        

        if formEdit.is_valid():
            user = User.objects.get(username=usuario)
            
            user.email = formEdit.cleaned_data.get('email')
            user.first_name = formEdit.cleaned_data.get('first_name')
            user.last_name = formEdit.cleaned_data.get('last_name')
            
            formEdit.save()
            messages.success(request, 'Tu perfil ha sido actualizado.')
            return redirect(reverse_lazy('edicion_perfil'))
    else:
        formEdit = UserEditForm(instance=usuario)

    return render(request, 'Aplicacion_Inventario/editar_perfil.html', {'form': formEdit})


# ------------------------------------ Cambio de clave ---------------------------------------------
class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = 'Aplicacion_Inventario/cambio_clave.html'
    success_url = reverse_lazy('index')


# ------------------------------------ Agregar Avatar ---------------------------------------------
@login_required
def agregar_avatar(request):
    if request.method == 'POST':
        formAvatar = AvatarForm(request.POST)
        
        if formAvatar.is_valid():
            user = User.objects.get(username=request.user)
            #___Borrar avatares viejos
            avatarViejo = Avatar.objects.filter(user=request.user)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            #-------------------------------------------------------
            avatar = Avatar(user=request.user, 
                            imagen= formAvatar.cleaned_data['imagen'])
            avatar.save()
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session['avatar'] = imagen
            print(f"{imagen}")
            return redirect(reverse_lazy('index'))
    else:
        formAvatar = AvatarForm()
        
    return render(request, 'Aplicacion_Inventario/agregar_avatar.html', {'form': formAvatar})
        

# ------------------------------------ Página Principal ---------------------------------------------
@login_required
def index(request):
    contexto = {
        'current_user': request.user,
        'conteo_personas': Persona.objects.count(),
        'conteo_notebooks': Notebook.objects.count(),
        'conteo_computadoras': Computadora.objects.count(),
        'conteo_marcas_perifericos': (Mouse.objects.count()) + (Headset.objects.count()),
        'conteo_campanias': Campania.objects.count(),
        'current_date': current_date 
    }

    return render(request, 'Aplicacion_Inventario/index.html', contexto)


# ------------------------------------ Notebooks ---------------------------------------------

#CRUD: 'Crear' y 'Buscar (read) están definidas en esta función!
@login_required
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
                    'current_user': request.user,
                    'current_date': current_date}
    else:
        contexto = {
                    'notebooks': Notebook.objects.all().order_by('id'), 
                    'miFormularioNotebook': miFormularioNotebook, 
                    'current_user': request.user,
                    'current_date': current_date}
    
    return render(request, 'Aplicacion_Inventario/notebooks.html', contexto)

class NotebookUpdate(LoginRequiredMixin, UpdateView): #CRUD: Update
    model = Notebook
    fields = ['nombre_notebook', 'nombre_notebook', 'marca_notebook', 'numero_serie_notebook', 
                  'modelo_notebook', 'estado_notebook']
    success_url = reverse_lazy('notebooks')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_user'] = self.request.user
        return context

class NotebookDelete(LoginRequiredMixin, DeleteView): #CRUD: Delete
    model = Notebook
    success_url = reverse_lazy('notebooks')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_user'] = self.request.user
        return context


# ------------------------------------ Campañas ---------------------------------------------

#CRUD: 'Crear' y 'Buscar (read) están definidas en esta función!
@login_required
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
                    'current_user': request.user,
                    'current_date': current_date}
    else:
        contexto = {
                    'campanias': Campania.objects.all().order_by('id'), 
                    'miFormularioCampania': miFormularioCampania, 
                    'current_user': request.user,
                    'current_date': current_date}
    
    
    return render(request, 'Aplicacion_Inventario/campanias.html', contexto)

class CampaniaUpdate(LoginRequiredMixin, UpdateView): #CRUD: Update
    model = Campania
    fields = ['nombre_campania', 'descripcion_campania']
    success_url = reverse_lazy('campanias')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_user'] = self.request.user
        return context
    
class CampaniaDelete(LoginRequiredMixin, DeleteView): #CRUD: Delete
    model = Campania
    success_url = reverse_lazy('campanias')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_user'] = self.request.user
        return context


# ------------------------------------ PC's ---------------------------------------------

#CRUD: 'Crear' y 'Buscar (read) están definidas en esta función!
@login_required
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
                    'current_user': request.user,
                    'current_date': current_date}
    else:
        contexto = {
                    'computadoras': Computadora.objects.all().order_by('id'), 
                    'miFormularioComputadora': miFormularioComputadora, 
                    'current_user': request.user,
                    'current_date': current_date}
    
    
    return render(request, 'Aplicacion_Inventario/computadoras_escritorio.html', contexto)

class ComputadoraUpdate(LoginRequiredMixin, UpdateView): #CRUD: Update
    model = Computadora
    fields = ['nombre_computadora', 'version_windows', 'estado_computadora_escritorio']
    success_url = reverse_lazy('computadoras')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_user'] = self.request.user
        return context
    
class ComputadoraDelete(LoginRequiredMixin, DeleteView): #CRUD: Delete
    model = Computadora
    success_url = reverse_lazy('computadoras')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_user'] = self.request.user
        return context

# ------------------------------------ Perifericos ---------------------------------------------

#CRUD: 'Crear' y 'Buscar (read) están definidas en esta función!
@login_required
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
        'current_user': request.user,
        'current_date': current_date
    }
    
    return render(request, 'Aplicacion_Inventario/perifericos.html', contexto)

# ----- Mouse ---------------------------------------------
class MouseUpdate(LoginRequiredMixin, UpdateView): #CRUD: Update
    model = Mouse
    fields = ['marca_mouse']
    success_url = reverse_lazy('perifericos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_user'] = self.request.user
        return context
    
class MouseDelete(LoginRequiredMixin, DeleteView): #CRUD: Delete
    model = Mouse
    success_url = reverse_lazy('perifericos')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_user'] = self.request.user
        return context

# ----- Headset ---------------------------------------------
class HeadsetUpdate(LoginRequiredMixin, UpdateView): #CRUD: Update
    model = Headset
    fields = ['marca_headset']
    success_url = reverse_lazy('perifericos')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_user'] = self.request.user
        return context
    
class HeadsetDelete(LoginRequiredMixin, DeleteView): #CRUD: Delete
    model = Headset
    success_url = reverse_lazy('perifericos')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_user'] = self.request.user
        return context


# ------------------------------------ Personas ---------------------------------------------

#CRUD: 'Crear' y 'Buscar (read) están definidas en esta función!
@login_required
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
        'current_user': request.user,
        'current_date': current_date
    }
    
    return render(request, 'Aplicacion_Inventario/personas.html', contexto)

class PersonaUpdate(LoginRequiredMixin, UpdateView): #CRUD: Update
    model = Persona
    fields = ['nombre_persona', 'apellido_persona', 'cuit_persona', 'email_persona', 
                'id_notebook', 'id_computadora_escritorio', 
                'id_campania', 'id_headset', 'id_mouse']
    success_url = reverse_lazy('personas')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_user'] = self.request.user
        return context
    
class PersonaDelete(LoginRequiredMixin, DeleteView): #CRUD: Delete
    model = Persona
    success_url = reverse_lazy('personas')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_user'] = self.request.user
        return context




