from django.urls import path, include
from .views import *

urlpatterns = [
    
    # ------------------------------------ Página Prncipal ---------------------------------------------
    path('', index, name="index"),
    
    # ------------------------------------ Notebooks ---------------------------------------------
    path('notebooks/', notebooks, name="notebooks"),
    path('notebooks-update/<int:pk>/', NotebookUpdate.as_view(), name="notebook_update"),
    path('notebooks-delete/<int:pk>/', NotebookDelete.as_view(), name="notebook_delete"),
    
    # ------------------------------------ Campañas ---------------------------------------------
    path('campañas/', campanias, name="campanias"),
    path('campañas-update/<int:pk>/', CampaniaUpdate.as_view(), name="campania_update"),
    path('campañas-delete/<int:pk>/', CampaniaDelete.as_view(), name="campania_delete"),
    
    # ------------------------------------ Usuarios ---------------------------------------------
    path('usuarios/', personas, name="personas"),
    path('usuarios-update/<int:pk>/', PersonaUpdate.as_view(), name="persona_update"),
    path('usuarios-delete/<int:pk>/', PersonaDelete.as_view(), name="persona_delete"),
    
    # ------------------------------------ Perifericos ---------------------------------------------
    path('perifericos/', perifericos, name="perifericos"),
    
    # ----- Mouse ---------------------------------------------
    path('mouses-update/<int:pk>/', MouseUpdate.as_view(), name="mouse_update"),
    path('mouses-delete/<int:pk>/', MouseDelete.as_view(), name="mouse_delete"),
    # ----- Headset ---------------------------------------------
    path('headsets-update/<int:pk>/', HeadsetUpdate.as_view(), name="headset_update"),
    path('headsets-delete/<int:pk>/', HeadsetDelete.as_view(), name="headset_delete"),
    
    # ------------------------------------ PC's ---------------------------------------------
    path('computadoras/', computadoras_escritorio, name="computadoras"),
    path('computadoras-update/<int:pk>/', ComputadoraUpdate.as_view(), name="computadora_update"),
    path('computadoras-delete/<int:pk>/', ComputadoraDelete.as_view(), name="computadora_delete"),
    
    # ------------------------------------ Login (Aún no implementado) ---------------------------------------------
    path('login/', login, name='login_sistema')
]