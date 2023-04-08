from django.urls import path
from AppInicio.views import primer_template,mostrar_m,mi_vista


urlpatterns = [
    path('',mi_vista),
    path('tem/',primer_template),
    path('m/',mostrar_m),
]
