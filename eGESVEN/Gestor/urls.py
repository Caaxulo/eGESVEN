from django.urls import path
from . import views

app_name = 'Gestor'

urlpatterns = [
    path('', views.login_view, name='home'),
    path('productos/', views.lista_producto, name='lista_producto'),
    path('productos/<int:pk>/', views.detalle_producto, name='detalle_producto'),
    path('productos/<int:pk>/eliminar/', views.eliminar_producto, name='eliminar_producto'),
    path('productos/login/', views.login_view, name='login'),  
    path('productos/register/', views.register_view, name='register'),  
]