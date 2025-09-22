"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
    path("", views.VistaIndice.as_view(), name="inicio"),  # Listado de encuestas
    path("crear/", views.crear_pregunta, name="crear_pregunta"),  # Crear nueva pregunta
    path("<int:pk>/modificar/", views.VistaModificarPregunta.as_view(), name="modificar_pregunta"),  # Modificar pregunta
    path("<int:pregunta_id>/eliminar/", views.eliminar_pregunta, name="eliminar_pregunta"),  # Eliminar pregunta
    path("<int:pk>/", views.VistaDetalle.as_view(), name="detalle"),  # Detalle de la pregunta
    path("<int:pk>/resultados/", views.VistaResultados.as_view(), name="resultados"),  # Resultados
    path("<int:pregunta_id>/votar/", views.votar, name="votar"),  # Votar
    path("<int:pregunta_id>/agregar_opcion/", views.agregar_opcion, name="agregar_opcion"),  # Agregar opción
]
