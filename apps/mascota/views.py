from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
# importar clase
from django.http import HttpResponse
from apps.mascota.forms import MascotaForm
from apps.mascota.models import Mascota

# Create your views here.

def index(request):
    return render(request,'mascota/index.html')

# DESDE AQUI VISTAS BASADAS EN funciones
def mascota_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mascota_listar')
    else:
        form = MascotaForm()

    return render(request,'mascota/mascota_form.html', {'form':form})

# FUNCION PARA LISTAR UNA MASCOTA
def mascota_list(request):
    # ordenar por id
    mascota = Mascota.objects.all().order_by('id')
    contexto = {'mascotas':mascota}
    return render(request,'mascota/mascota_list.html',contexto)

# FUNCION PARA EDITAR UNA MASCOTA

def mascota_edit(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'GET':
        form =MascotaForm(instance=mascota)
    else:
        form=MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
        return redirect('mascota_listar')
        
    return render(request,'mascota/mascota_form.html',{'form':form})

# FUNCION PARA ELMINAR UNA MASCOTA
def mascota_delete(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'POST':
        mascota.delete()
        return redirect('mascota_listar')
        
    return render(request,'mascota/mascota_delete.html',{'mascota':mascota})

# DESDE AQUI VISTAS BASADAS EN CLASES

class MascotaList(ListView):
    model=Mascota
    template_name='mascota/mascota_list.html'

class MascotaCreate(CreateView):
    model=Mascota
    form_class=MascotaForm
    template_name='mascota/mascota_form.html'
    success_url=reverse_lazy('mascota_listar')

class MascotaUpdate(UpdateView):
    model=Mascota
    form_class=MascotaForm
    template_name='mascota/mascota_form.html'
    success_url=reverse_lazy('mascota_listar')


class MascotaDelete(DeleteView):
    model=Mascota
    template_name='mascota/mascota_delete.html'
    success_url=reverse_lazy('mascota_listar')