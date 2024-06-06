#agrego get_object_or_404 , redirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
#agrego contacto
from .models import Proyecto, Contacto
from .forms import ContactoForm

# Create your views here que el inicio que muestra los proyectos 
def home(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'index.html', {'proyectos':proyectos})

#4 agrego por acá
def contacto_nuevo(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacto_confirmacion')
    else:
        form = ContactoForm()
    return render(request, 'myportfolio/contacto_formulario.html', {'form': form})

@login_required
def contacto_detalle(request,pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    return render(request, 'myportfolio/contacto_detalle.html', {'contacto': contacto})

@login_required
def contacto_editar(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)  # Obtén el objeto Contacto con la clave primaria (pk) especificada, o devuelve un 404 si no existe.
    if request.method == "POST":
        form = ContactoForm(request.POST, instance=contacto)  # Crea una instancia del formulario con los datos POST y el contacto existente.
        if form.is_valid():
            form.save()  # Guarda los cambios en el objeto Contacto.
            return redirect('contacto_detalle', pk=contacto.pk)  # Redirige a la vista contacto_detalle después de guardar.
    else:
        form = ContactoForm(instance=contacto)  # Crea una instancia del formulario con el contacto existente.
    return render(request, 'myportfolio/contacto_formulario.html', {'form': form})  # Renderiza la plantilla contacto_formulario.html con el formulario.

@login_required
def contacto_eliminar(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    contacto.delete()
    return redirect('contacto_lista')

login_required
def contacto_lista(request):
    contactos = Contacto.objects.all()
    return render (request, 'myportfolio/contacto_lista.html', {'contactos': contactos})

def contacto_confirmacion(request):
    return render(request, 'myportfolio/contacto_confirmacion.html')


