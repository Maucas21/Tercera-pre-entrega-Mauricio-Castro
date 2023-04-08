from django.shortcuts import render,redirect

# Create your views here.

def mi_vista(request):
    
    return render(request, r"appinicio/index.html")
    
    
def primer_template(request):
    
    datos = {"nombre":"juanito"}
    
    return render(request, r"appinicio/primer_template.html",datos)

def mostrar_m(request):
    
    datos = {"m":"es un lindo dia"}
    
    return render(request, r"appinicio/mostrar_m.html",datos)