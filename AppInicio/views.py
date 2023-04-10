from django.shortcuts import render,redirect
from datetime import datetime
from AppInicio.models import Tarea
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView


# Create your views here.

class Logueo(LoginView):
    template_name = r"appinicio/login.html"
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy("pendientes")


def Inicio(request):
    
    return render(request, r"appinicio/index.html")
    
    
def primer_template(request):
    
    datos = {"nombre":"juanito"}
    
    return render(request, r"appinicio/primer_template.html",datos)

def mostrar_m(request):
    
    # datos = {"m":"es un lindo dia"}
    
    return render(request, r"appinicio/mostrar_m.html")


class ListaPendientes(ListView):
    model = Tarea
    template_name = "appinicio/lista_tareas.html"

    
class DetalleTarea(DetailView):
    model = Tarea
    template_name = "appinicio/tarea.html"
    context_object_name = "tarea"
    
    
class CrearTarea(CreateView):
    model = Tarea
    template_name = "appinicio/crear_tarea.html"
    fields = '__all__'
    success_url = reverse_lazy("pendientes")
    

class EditarTarea(UpdateView):
    model = Tarea
    template_name = "appinicio/crear_tarea.html"
    fields = '__all__'
    success_url = reverse_lazy("pendientes")
    
    
class EliminarTarea(DeleteView):
    model = Tarea
    template_name = "appinicio/eliminar_tarea.html"
    context_object_name = "tarea"
    success_url = reverse_lazy("pendientes")
    
    
    
    
    