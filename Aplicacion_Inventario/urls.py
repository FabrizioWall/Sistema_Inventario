from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import *

urlpatterns = [
    
    # ------------------------------------ Página Prncipal ---------------------------------------
    path('PYDHome/', index, name="index"),
    
    # ------------------------------------ Notebooks ---------------------------------------------
    path('notebooks/', notebooks, name="notebooks"),
    path('notebooks-update/<int:pk>/', NotebookUpdate.as_view(), name="notebook_update"),
    path('notebooks-delete/<int:pk>/', NotebookDelete.as_view(), name="notebook_delete"),
    
    # ------------------------------------ Campañas ----------------------------------------------
    path('campañas/', campanias, name="campanias"),
    path('campañas-update/<int:pk>/', CampaniaUpdate.as_view(), name="campania_update"),
    path('campañas-delete/<int:pk>/', CampaniaDelete.as_view(), name="campania_delete"),
    
    # ------------------------------------ Usuarios ----------------------------------------------
    path('usuarios/', personas, name="personas"),
    path('usuarios-update/<int:pk>/', PersonaUpdate.as_view(), name="persona_update"),
    path('usuarios-delete/<int:pk>/', PersonaDelete.as_view(), name="persona_delete"),
    
    # ------------------------------------ Perifericos -------------------------------------------
    path('perifericos/', perifericos, name="perifericos"),
    
    # _____ Mouse ---------------------------------------------
    path('mouses-update/<int:pk>/', MouseUpdate.as_view(), name="mouse_update"),
    path('mouses-delete/<int:pk>/', MouseDelete.as_view(), name="mouse_delete"),
    # _____ Headset ---------------------------------------------
    path('headsets-update/<int:pk>/', HeadsetUpdate.as_view(), name="headset_update"),
    path('headsets-delete/<int:pk>/', HeadsetDelete.as_view(), name="headset_delete"),
    
    # ------------------------------------ PC's ---------------------------------------------------
    path('computadoras/', computadoras_escritorio, name="computadoras"),
    path('computadoras-update/<int:pk>/', ComputadoraUpdate.as_view(), name="computadora_update"),
    path('computadoras-delete/<int:pk>/', ComputadoraDelete.as_view(), name="computadora_delete"),
    
    # ----------------------------- Login, Logout, Registro ----------------------------------------
    path('', login_request, name='login_sistema'),
    path('logout/', LogoutView.as_view(template_name="Aplicacion_Inventario/logout.html"), 
            name='logout_sistema'),
    path('registro-usuario/', registro_request, name='registro_sistema'),
    
    # ------------------------------------ Exportar ------------------------------------------------
    path('exportar-personas/', exportar_personas, name='exportar_personas'),
    path('exportar-notebooks/', exportar_notebooks, name='exportar_notebooks'),
    path('exportar-computadoras/', exportar_computadoras, name='exportar_computadoras'),
    path('exportar-headset/', exportar_headset, name='exportar_headset'),
    path('exportar-mouse/', exportar_mouse, name='exportar_mouse'),
    path('exportar-campañas/', exportar_campanias, name='exportar_campanias'),
    
    # ------------------------------------ TXT de Formato mail -------------------------------------
    path('mail-txt/<int:persona_id>/', notas_mail, name='mail_txt'),
    
    # ---------------------- Edición Perfil, Cambio Clave, Cambio Avatar ---------------------------
    path('perfil/', profile, name='edicion_perfil'),
    path('<int:pk>/password/', CambiarClave.as_view(), name='cambiar_clave'),
    path('agregar_avatar/', agregar_avatar, name='agregar_avatar')
]