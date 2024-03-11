from django.shortcuts import render, get_object_or_404
from .models import * 
from .forms import *

def home(request):
    return render(request, "aplicacion/index.html")

#______________________________________________________ usuarios
def usuario(request):
    contexto = {'usuarios': Usuario.objects.all()}
    return render(request, "aplicacion/usuario.html", contexto)

def nuevo_usuario(request):
    if request.method == "POST":
        miForm = UsuarioForm(request.POST)
        if miForm.is_valid():
            u_nombre= miForm.cleaned_data.get("nombre")
            u_email = miForm.cleaned_data.get("email")
            usuario = Usuario(nombre=u_nombre, email=u_email)
            usuario.save()
            return render(request, "aplicacion/index.html")
    else:
        miForm = UsuarioForm()
    return render(request, "aplicacion/nuevo_usuario.html", {"form": miForm})

#______________________________________________________ reseñas
def review(request):
    return render(request, "aplicacion/review.html")

def nuevo_review(request):
    if request.method == "POST":
        miForm = ReviewForm(request.POST)
        if miForm.is_valid():
            r_alojamiento = miForm.cleaned_data.get("alojamiento")
            r_texto = miForm.cleaned_data.get("texto")
            r_calificacion = miForm.cleaned_data.get("calificacion")
            r_usuario = miForm.cleaned_data.get("usuario")
            review = Review(alojamiento=r_alojamiento, texto=r_texto, calificacion=r_calificacion, usuario=r_usuario)
            review.save()
            return render(request, "aplicacion/index.html")
    else:
        miForm = ReviewForm()
    return render(request, "aplicacion/nuevo_review.html", {"form": miForm})

#______________________________________________________ alojamientos
def alojamiento(request):
    contexto = {'alojamiento': Alojamiento.objects.all()}
    return render(request, "aplicacion/alojamiento.html", contexto)

def detalle_alojamiento(request, alojamiento_id):
    alojamiento = get_object_or_404(Alojamiento, id=alojamiento_id)
    return render(request, 'aplicacion/detalle_alojamiento.html', {'alojamiento': alojamiento})

def nuevo_alojamiento(request):
    if request.method == "POST":
        miForm = AlojamientoForm(request.POST)
        if miForm.is_valid():
            aloj_titulo = miForm.cleaned_data.get("titulo")
            aloj_descripcion = miForm.cleaned_data.get("descripcion")
            aloj_ciudad = miForm.cleaned_data.get("ciudad")
            aloj_direccion = miForm.cleaned_data.get("direccion")
            aloj_precio = miForm.cleaned_data.get("precio")
            alojamiento = Alojamiento(titulo=aloj_titulo, descripcion=aloj_descripcion, ciudad=aloj_ciudad, direccion=aloj_direccion, precio=aloj_precio)
            alojamiento.save()
            return render(request, "aplicacion/index.html")
    else:
        miForm = AlojamientoForm()
    return render(request, "aplicacion/nuevo_alojamiento.html", {"form": miForm})

#______________________________________________________ buscar alojamientos
def buscar_alojamiento(request):
    return render(request, "aplicacion/buscar_alojamiento.html")

def encontrar_alojamiento(request):
    if "buscar" in request.GET:
        patron = request.GET["buscar"]
        alojamiento = Alojamiento.objects.filter(ciudad__icontains=patron)
        contexto = {"alojamiento": alojamiento}
        return render(request, "aplicacion/alojamiento.html", contexto)
    
    contexto = {"alojamiento": Alojamiento.objects.all()}
    return render(request, "aplicacion/alojamiento.html", contexto)
