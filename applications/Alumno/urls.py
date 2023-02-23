from django.contrib import admin
from django.urls import path, re_path, include
from . import views



app_name = 'alumno_app'

urlpatterns = [
    
    path(
        'alumno/create/', #se detalla que registro segun su clave primaria desea detallar
        views.AlumnoCreateView.as_view(),
        name='Creacion de Alumno',
    ),
    path(
        'alumno/panel/',
        views.Panel.as_view(),
        name='panel-alumno'
    ),
    path(
        "login/",
        views.LoginUser.as_view(),
        name="login-alumno"
    ),
       path(
        "alumno/logout/",
        views.LogoutView.as_view(),
        name="logout-alumno"
    ),
    path(
        "alumno/update/<pk>",
        views.AlumnoUpdateView.as_view(),
        name="Modificar Alumno"
    ),
    path(
        "alumno/detail/<pk>",
        views.AlumnoDetail.as_view(),
        name="Detalles de Alumno"
    ),
    path(
        "alumno/delete/<pk>",
        views.AlumnoUpdateView.as_view(),
        name="Borrar Alumno"
    ),
]