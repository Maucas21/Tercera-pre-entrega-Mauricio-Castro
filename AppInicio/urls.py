from django.urls import path
from AppInicio.views import primer_template,mostrar_m,Inicio


urlpatterns = [
    path('',Inicio, name="inicio"),
    path('tem/',primer_template, name="tem"),
    path('m/',mostrar_m,name="m"),   
]
