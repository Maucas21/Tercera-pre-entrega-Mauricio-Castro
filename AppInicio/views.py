from django.shortcuts import render,redirect
from datetime import datetime
from AppInicio.models import Tarea
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class Logueo(LoginView):
    template_name = r"appinicio/login.html"
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy("pendientes")


class PaginaRegistro(FormView):
    
    template_name = "appinicio/registro.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("pendientes")
    
    def form_valid(self, form):
        usuario = form.save()
        if usuario is not None:
            login(self.request, usuario)
        return super(PaginaRegistro, self).form_valid(form)
    
        def get(self, *args, **kwargs):
            if self.request.user.is_authenticated:
                return redirect('pendientes')
        return super(PaginaRegistro, self).get(*args, **kwargs)


def Inicio(request):
    
    return render(request, r"appinicio/index.html")
    

def mostrar(request):
    
    # datos = {"m":"es un lindo dia"}
    
    return render(request, r"appinicio/mostrar.html")


class ListaPendientes(LoginRequiredMixin,ListView):
    model = Tarea
    template_name = "appinicio/lista_tareas.html"
    context_object_name = "tareas"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tareas"] = context["tareas"].filter(usuario=self.request.user)
        context["count"] = context["tareas"].filter(completo=False).count()
        
        valor_buscar = self.request.GET.get("area-buscar") or ""
        
        if valor_buscar: 
            context["tareas"] = context["tareas"].filter(titulo__icontains=valor_buscar) 
            
        context["valor_buscar"] = valor_buscar
            
        return context
    

class DetalleTarea(LoginRequiredMixin,DetailView):
    model = Tarea
    template_name = "appinicio/tarea.html"
    context_object_name = "tareas"
    
    
class CrearTarea(LoginRequiredMixin,CreateView):
    model = Tarea
    template_name = "appinicio/crear_tarea.html"
    fields = ["titulo","descripcion","completo"]
    success_url = reverse_lazy("pendientes")
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super(CrearTarea, self).form_valid(form)
    

class EditarTarea(LoginRequiredMixin,UpdateView):
    model = Tarea
    template_name = "appinicio/crear_tarea.html"
    fields = ["titulo","descripcion","completo"]
    success_url = reverse_lazy("pendientes")
    
    
class EliminarTarea(LoginRequiredMixin,DeleteView):
    model = Tarea
    template_name = "appinicio/eliminar_tarea.html"
    context_object_name = "tareas"
    success_url = reverse_lazy("pendientes")
    
    
    
    
    