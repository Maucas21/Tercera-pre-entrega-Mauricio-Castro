from django.urls import path
from AppInicio.views import primer_template,mostrar_m,Inicio,ListaPendientes,DetalleTarea,CrearTarea,EditarTarea,EliminarTarea,Logueo
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',Inicio, name="inicio"),
    path('login',Logueo.as_view(),name="login"),
    path('logout',LogoutView.as_view(next_page="login"),name="logout"),
    path('tem/',primer_template, name="tem"),
    path('m/',mostrar_m,name="m"),
    path('pendientes/',ListaPendientes.as_view(),name="pendientes"),
    path('tarea/<int:pk>',DetalleTarea.as_view(),name="tarea"),
    path('crear-tarea/',CrearTarea.as_view(),name="crear-tarea"),
    path('ediar-tarea/<int:pk>',EditarTarea.as_view(),name="editar-tarea"),
    path('eliminar-tarea/<int:pk>',EliminarTarea.as_view(),name="eliminar-tarea"),
]
