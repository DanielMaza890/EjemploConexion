from django.shortcuts import render, redirect, get_object_or_404
from .models import Duda, Respuesta

# Ver todas las dudas
def lista_dudas(request):
    dudas = Duda.objects.all().order_by('-fecha_creacion')
    return render(request, 'foro/lista_dudas.html', {'dudas': dudas})

# Crear una nueva duda (Alta)
def crear_duda(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        contenido = request.POST.get('contenido')
        Duda.objects.create(titulo=titulo, contenido=contenido)
        return redirect('lista_dudas')
    return render(request, 'foro/crear_duda.html')

# Ver detalle de una duda y agregar respuesta
def detalle_duda(request, duda_id):
    duda = get_object_or_404(Duda, id=duda_id)
    if request.method == 'POST':
        contenido_resp = request.POST.get('contenido')
        Respuesta.objects.create(duda=duda, contenido=contenido_resp)
        return redirect('detalle_duda', duda_id=duda.id)
    return render(request, 'foro/detalle_duda.html', {'duda': duda})

# Eliminar duda (Baja)
def eliminar_duda(request, duda_id):
    duda = get_object_or_404(Duda, id=duda_id)
    duda.delete()
    return redirect('lista_dudas')