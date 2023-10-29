from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
 


urlpatterns =[
    path('', views.index, name='index'),
    path('cambios/<str:num_holken>/', views.cambios_holken, name='cambios_holken'),
    path('minijuegos', views.mini_juegos, name='mini_juegos'),
    path('evaluador', views.evaluador, name='evaluador'),
    path('admin', views.admin, name='admin'),
    path('busqueda', views.busqueda_holken, name='busqueda_holken'),
    path('registro_holken/', views.registro_holken, name='registro_holken'),
    path('generar_grafico/', views.generar_grafico, name='generar_grafico'),

    

    path('lista_holken/', views.lista_holken, name='lista_holken')
   
]