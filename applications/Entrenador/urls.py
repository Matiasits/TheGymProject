from django.contrib import admin
from django.urls import path, re_path, include
from . import views

app_name = 'entrenador_app'


urlpatterns = [
  path(
        'entrenador/create/', #se detalla que registro segun su clave primaria desea detallar
        views.EntrenadorCreateView.as_view(),
        name='Creacion de Entrenador',
    ),
    path(
        'entrenador/panel/',
        views.Panel.as_view(),
        name='panel-entrenador'
    ),
    path(
        "login/",
        views.LoginUser.as_view(),
        name="login-entrenador"
    ),
       path(
        "entrenador/logout/",
        views.LogoutView.as_view(),
        name="logout-entrenador"
    ),
    path(
        "entrenador/update/<pk>",
        views.EntrenadorUpdateView.as_view(),
        name="Modificar Entrenador"
    ),
    path(
        "entrenador/detail/<pk>",
        views.EntrenadorDetail.as_view(),
        name="Detalles de Entrenador"
    ),
    path(
        "entrenador/delete/<pk>",
        views.EntrenadorDeleteView.as_view(),
        name="Borrar Entrenador"
    ),   
]