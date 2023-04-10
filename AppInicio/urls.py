from django.urls import path
from AppInicio.views import primer_template,mostrar_m,Inicio,ListaPendientes,DetalleTarea,CrearTarea


urlpatterns = [
    path('',Inicio, name="inicio"),
    path('tem/',primer_template, name="tem"),
    path('m/',mostrar_m,name="m"),
    path('pendientes/',ListaPendientes.as_view(),name="pendientes"),
    path('tarea/<int:pk>',DetalleTarea.as_view(),name="tarea"),
    path('crear-tarea/',CrearTarea.as_view(),name="crear-tarea"),
]
