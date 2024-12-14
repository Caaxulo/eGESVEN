from django.urls import path
from . import views

app_name = 'Gestor'

urlpatterns = [
    path('', views.redirigir_a_productos, name='home'),
    path('productos/', views.lista_producto, name='lista_producto'),
    path('productos/<int:pk>/', views.detalle_producto, name='detalle_producto'),
    path('productos/<int:pk>/eliminar/', views.eliminar_producto, name='eliminar_producto'),
]