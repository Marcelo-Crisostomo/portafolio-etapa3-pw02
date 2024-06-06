from django.urls import path  # Importa la función path del módulo urls de Django, que se usa para definir rutas de URL.
from . import views  # Importa el módulo views desde el mismo directorio, donde se definen las funciones que manejan las vistas.

urlpatterns = [
    path('', views.home, name='home'),  # Define una ruta de URL. La cadena vacía ('') indica la raíz del sitio web. Esta ruta llama a la función home en views y le asigna el nombre 'home'.
    path('contacto/nuevo/', views.contacto_nuevo, name='contacto_nuevo'),
    path('contacto/<int:pk>/', views.contacto_detalle, name='contacto_detalle'),
    path('contacto/<int:pk>/editar/', views.contacto_editar, name='contacto_editar'),
    path('contacto/<int:pk>/eliminar/', views.contacto_eliminar, name='contacto_eliminar'),
    path('contactos/', views.contacto_lista, name='contacto_lista'),
    path('contacto/confirmacion/', views.contacto_confirmacion, name='contacto_confirmacion'),
]
