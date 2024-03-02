from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('notebooks/', notebooks, name="notebooks"),
    path('campañas/', campanias, name="campanias"),
    path('usuarios/', personas, name="personas"),
    path('perifericos/', perifericos, name="perifericos"),
    path('agregar-notebook/', agregar_notebook, name='agregar_notebook'),
    path('eliminar-notebook/', eliminar_notebook, name='eliminar_notebook'),
    path('actualizar-notebook', actualizar_notebook, name='actualizar_notebook')
]