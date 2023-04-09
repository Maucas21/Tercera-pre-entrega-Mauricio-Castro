from django.shortcuts import render,redirect
from datetime import datetime

# Create your views here.

def Inicio(request):
    
    return render(request, r"appinicio/index.html")
    
    
def primer_template(request):
    
    datos = {"nombre":"juanito"}
    
    return render(request, r"appinicio/primer_template.html",datos)

def mostrar_m(request):
    
    datos = {"m":"es un lindo dia"}
    
    return render(request, r"appinicio/mostrar_m.html",datos)

# def mostrar_fecha(request):
#     dt = datetime.now()
#     dt_formateado = dt.strftime ("%A %d %B %Y %I :%M")
#     fecha = {"fecha":dt_formateado}

#     return render(request, r"appinicio/mostrar_fecha.html",fecha)

# def data_time(request):
#     current_datetime = datetime.now()
#     return render(request, 'appinicio/data_time.html', {'current_datetime': current_datetime})
