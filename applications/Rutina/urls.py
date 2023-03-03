from django.contrib import admin
from django.urls import path, re_path, include
from . import views

app_name = 'rutina_app'

urlpatterns = [
  path(
        'rutina/create/', #se detalla que registro segun su clave primaria desea detallar
        views.RutinaCreateView.as_view(),
        name='Creacion de Rutina',
    ),
    path(
        'rutina/panel/',
        views.Panel.as_view(),
        name='panel-rutina'
    ),
    path(
        "login/",
        views.LoginUser.as_view(),
        name="login-rutina"
    ),
       path(
        "rutina/logout/",
        views.LogoutView.as_view(),
        name="logout-rutina"
    ),
    path(
        "rutina/update/<pk>",
        views.RutinaUpdateView.as_view(),
        name="Modificar Rutina"
    ),
    path(
        "rutina/detail/<pk>",
        views.RutinaDetail.as_view(),
        name="Detalles de Rutina"
    ),
    path(
        "rutina/delete/<pk>",
        views.RutinaDeleteView.as_view(),
        name="Borrar Rutina"
    ),
]