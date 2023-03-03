from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from .models import Entrenador
from .form import LoginForm, EntrenadorForm
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
    success_url = reverse_lazy('entrenador_app:panel-entrenador')
    context_object_name = 'login'
    
    def form_valid(self, form):
        user = authenticate(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password']
            )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)


class Panel(ListView):
    model = Entrenador
    template_name = 'entrenador/panel.html'
    context_object_name = 'entrenador'
    paginate_by = 5

    
    def get_queryset(self):
        #definimos variables donde obtendremos los request
        dato = self.request.GET.get('dato','')
        #del model Entrenador filtramos los atributos que necesitamos
        lista = Entrenador.objects.filter(dni__icontains = dato) | Entrenador.objects.filter(nombre__icontains = dato) | Entrenador.objects.filter(apellido__icontains = dato)
        return lista
    
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'entrenador_app:login-entrenador'
            )
        )


############################ VIEWS ####################################
class EntrenadorDetail(LoginRequiredMixin,DetailView):  #DETALLES
    model = Entrenador
    template_name = "entrenador/detail.html"
    context_object_name = "detail"
    login_url = reverse_lazy('entrenador_app:login-entrenador')



class EntrenadorCreateView(LoginRequiredMixin,CreateView):    #CREACION
    model = Entrenador
    template_name = "entrenador/create.html"
    form_class = EntrenadorForm
    login_url = reverse_lazy('entrenador_app:login-entrenador')
    success_url = reverse_lazy('entrenador_app:panel-entrenador')
    

    def form_valid(self, form):
        entrenador = form.save(commit=False)
        entrenador.nombre_completo = f"{entrenador.nombre} {entrenador.apellido}"
        entrenador.save()

        return super(EntrenadorCreateView, self).form_valid(form)
    
    
class EntrenadorUpdateView(LoginRequiredMixin,UpdateView):    #ACTUALIZACION
    model = Entrenador
    template_name = "entrenador/update.html"
    form_class = EntrenadorForm
    login_url = reverse_lazy('entrenador_app:login-entrenador')
    success_url = reverse_lazy('entrenador_app:panel-entrenador')

    def form_valid(self, form):
        entrenador = form.save(commit=False)
        entrenador.nombre_completo = f"{entrenador.nombre} {entrenador.apellido}"
        entrenador.save()

        return super(EntrenadorUpdateView, self).form_valid(form)


class EntrenadorDeleteView(LoginRequiredMixin,DeleteView,DetailView):
    model = Entrenador
    template_name = "entrenador/delete.html"
    context_object_name = "delete_detail"
    login_url = reverse_lazy('entrenador_app:login-entrenador')
    success_url = reverse_lazy('entrenador_app:panel-entrenador')
