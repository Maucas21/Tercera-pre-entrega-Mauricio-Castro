from django.urls import path
from AppInicio.views import primer_template,mostrar_m


urlpatterns = [
    path('tem/',primer_template),
    path('m/',mostrar_m),
]
