from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from .models import Alumno
from .form import LoginForm, AlumnoForm 
from django.views.generic import (
    View,
    ListView,
    DeleteView,
    CreateView,
    TemplateView,
    UpdateView,
    DetailView
)
from django.views.generic.edit import (
    FormView
)

############################ LOGIN ####################################
class LoginUser(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('alumno_app:panel-alumno')
    context_object_name = 'login'
    
    def form_valid(self, form):
        user = authenticate(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password']
            )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)


class Panel(ListView):
    model = Alumno
    template_name = 'alumno/panel.html'
    context_object_name = 'alumnos'
    paginate_by = 5

    
    def get_queryset(self):
        #definimos variables donde obtendremos los request
        dato = self.request.GET.get('dato','')
        #del model Alumno filtramos los atributos que necesitamos
        lista = Alumno.objects.filter(dni__icontains = dato) | Alumno.objects.filter(nombre__icontains = dato) | Alumno.objects.filter(apellido__icontains = dato)
        return lista
    
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'alumno_app:login-alumno'
            )
        )


############################ VIEWS ####################################
class AlumnoDetail(LoginRequiredMixin,DetailView):  #DETALLES
    model = Alumno
    template_name = "alumno/detalles.html"
    context_object_name = "detalle"
    login_url = reverse_lazy('alumno_app:login-alumno')



class AlumnoCreateView(LoginRequiredMixin,CreateView):    #CREACION
    model = Alumno
    template_name = "alumno/create.html"
    form_class = AlumnoForm
    login_url = reverse_lazy('alumno_app:login-alumno')
    success_url = reverse_lazy('alumno_app:panel-alumno')
    

    def form_valid(self, form):
        alumno = form.save(commit=False)
        alumno.nombre_completo = f"{alumno.nombre} {alumno.apellido}"
        alumno.save()

        return super(AlumnoCreateView, self).form_valid(form)
    
    
class AlumnoUpdateView(LoginRequiredMixin,UpdateView):    #ACTUALIZACION
    model = Alumno
    template_name = "alumno/update.html"
    form_class = AlumnoForm
    login_url = reverse_lazy('alumno_app:login-alumno')
    success_url = reverse_lazy('alumno_app:panel-alumno')

    def form_valid(self, form):
        alumno = form.save(commit=False)
        alumno.nombre_completo = f"{alumno.nombre} {alumno.apellido}"
        alumno.save()

        return super(AlumnoUpdateView, self).form_valid(form)


class AlumnoDeleteView(LoginRequiredMixin,DeleteView,DetailView):
    model = Alumno
    template_name = "alumno/delete.html"
    context_object_name = "delete_detail"
    login_url = reverse_lazy('alumno_app:login-alumno')
    success_url = reverse_lazy('alumno_app:panel-alumno')
