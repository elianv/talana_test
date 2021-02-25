from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registro', views.registro_user, name='registro'),
    path('notificacion/<int:id>', views.notificacion, name='notificacion'),
    path('activar_cuenta/<int:id>/', views.activar_cuenta, name='activar_cuenta'),
    path('sorteo', views.ver_sorteo, name='sorteo'),
    path('ganador', views.ganador),
]