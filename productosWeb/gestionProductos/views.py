from django.shortcuts import render
from django.http import httpResponse
from gestionProductos.models import Articulos
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def buscar_productos(request):
    return (request,"busq_producto.html")

# def btn_buscar(request):
#     if request.get("texto_busasqueda"):
#       mensaje="Producto Buscado:%r" %request.get("texto_busasqueda")
#     else:
#        mensaje="Che has introducido nada"  
#     return httpResponse(mensaje)

def btn_buscar(request):
    nombreBuscado=request.get("texto_busasqueda")
    if nombreBuscado:
        articulos=Articulos.objects.filter(nombre__icontains=nombreBuscado)  # icontains=like
        return render(request,"resultado_busqueda.html", {"articulos":articulos, "query":nombreBuscado})
    else:
       mensaje="Che has introducido nada"  
       return httpResponse(mensaje)
    
def contacto(request):
    if request.method()=="POST": #se activa cuando el usuario envia la informacion
        #enviar un mail
        subject=request.get("asunto")
        email=request.get("email")
        message=request.get("mensaje") + " " + email
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["siagwebs@gmail.com"]
        send_mail(subject,message,email_from,recipient_list)
        return render(request,"gracias.html")
    
    return render(request,"contacto.html")


