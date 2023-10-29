from pyexpat.errors import messages
from django.http.response import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from .models import Holken
from .forms import HolkenForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
import matplotlib.pyplot as plt
from io import BytesIO
import base64


# Create your views here.

def index(request):
    return render(request,'index.html')

def cambios_holken(request, num_holken=None):
    num_holken = request.GET.get('num_holken', '') 
    try:
        holken = Holken.objects.get(id=num_holken)
    except Holken.DoesNotExist:
        raise Http404("Holken no encontrado")

    if request.method == 'POST':
        form = HolkenForm(request.POST, request.FILES, instance=holken)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirige a la página principal después de guardar los cambios

    else:
        form = HolkenForm(instance=holken)

    return HttpResponseRedirect(reverse('cambios_holken', args=[num_holken]))



    

def mini_juegos(request):
    return render(request, 'mini_juegos.html') 

def evaluador(request):
    return render(request, 'evaluador.html') 

def admin(request):
    return render(request, 'admin.html') 

def busqueda_holken(request):
    holken= Holken.objects.all,
    return render(request, 'busqueda_holken.html')


def lista_holken(request):
    holken = list(Holken.objects.values())
    data = {'holken':holken}
    return JsonResponse(data)

def registro_holken(request):
    if request.method == 'POST':
        form = HolkenForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Holken registrado con éxito.')
            return redirect('index')  # Redirige a la página de Principal
            
    else:
        form = HolkenForm()

    return render(request, 'registro_holken.html', {'form': form})



#Grafico tabla 

def generar_grafico(request):
    # Recupera los datos de la tabla tablaBody_holken
    data = tablaBody_holken.objects.all()

    # Procesa los datos para crear un gráfico
    x = [item.campo_x for item in data]  # Reemplaza 'campo_x' con el nombre real del campo
    y = [item.campo_y for item in data]  # Reemplaza 'campo_y' con el nombre real del campo

    # Crea un gráfico de barras
    plt.bar(x, y)
    plt.xlabel('Eje X')  # Personaliza las etiquetas de los ejes
    plt.ylabel('Eje Y')
    plt.title('Gráfico de Datos')

    # Guarda el gráfico en un objeto BytesIO
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    # Convierte el gráfico en datos base64
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png).decode()

    # Devuelve el gráfico en una página HTML
    return render(request, 'grafico.html', {'graphic': graphic})