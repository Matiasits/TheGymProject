from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from .models import Rutina
from .form import LoginForm, RutinaForm
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
    success_url = reverse_lazy('rutina_app:panel-rutina')
    context_object_name = 'login'
    
    def form_valid(self, form):
        user = authenticate(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password']
            )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)


class Panel(ListView):
    model = Rutina
    template_name = 'rutina/panel.html'
    context_object_name = 'rutina'
    paginate_by = 5

    
    def get_queryset(self):
        #definimos variables donde obtendremos los request
        dato = self.request.GET.get('dato','')
        #del model Rutina filtramos los atributos que necesitamos
        lista = Rutina.objects.filter(identificador_rutina__icontains = dato) | Rutina.objects.filter(tipo__icontains = dato)
        
        return lista
    
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'rutina_app:login-rutina'
            )
        )


############################ VIEWS ####################################
class RutinaDetail(LoginRequiredMixin,DetailView):  #DETALLES
    model = Rutina
    template_name = "rutina/detail.html"
    context_object_name = "detail"
    login_url = reverse_lazy('rutina_app:login-rutina')



class RutinaCreateView(LoginRequiredMixin,CreateView):    #CREACION
    model = Rutina
    template_name = "rutina/create.html"
    form_class = RutinaForm
    login_url = reverse_lazy('rutina_app:login-rutina')
    success_url = reverse_lazy('rutina_app:panel-Creacion de Rutina')    
    
class RutinaUpdateView(LoginRequiredMixin,UpdateView):    #ACTUALIZACION
    model = Rutina
    template_name = "rutina/update.html"
    form_class = RutinaForm
    login_url = reverse_lazy('rutina_app:login-rutina')
    success_url = reverse_lazy('rutina_app:Modificar Rutina')


class RutinaDeleteView(LoginRequiredMixin,DeleteView,DetailView):
    model = Rutina
    template_name = "rutina/delete.html"
    context_object_name = "delete_detail"
    login_url = reverse_lazy('rutina_app:login-rutina')
    success_url = reverse_lazy('rutina_app:Borrar Rutina')
    
