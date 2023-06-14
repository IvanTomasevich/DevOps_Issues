from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
# from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView

from .forms import *
# from Perfiles.models import Perfil


def registro(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            formulario.save()  # Esto lo puedo usar porque es un model form
            url_exitosa = reverse('home')
            return redirect(url_exitosa)
    else:  # GET
        formulario = UserRegisterForm()
    return render(request, 'Perfiles/registro.html', {'form': formulario})


def login_view(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            usuario = data.get('username')
            password = data.get('password')
            user = authenticate(username=usuario, password=password)
            # user puede ser un usuario o None
            if user:
                login(request=request, user=user)
                if next_url:
                    return redirect(next_url)
                url_exitosa = reverse('home')
                return redirect(url_exitosa)
    else:  # GET
        form = AuthenticationForm()
    return render(request, 'Perfiles/login.html', {'form': form})


class CustomLogoutView(LogoutView):
    template_name = 'Perfiles/logout.html'


class MiPerfilUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UserUpdateForm
    success_url = reverse_lazy('home')
    template_name = 'Perfiles/formulario_perfil.html'

    def get_object(self, queryset=None):
        return self.request.user


def agregar_avatar(request):
    if request.method == "POST":
        formulario = AvatarFormulario(request.POST, request.FILES)  # Aquí me llega toda la info del formulario html

        if formulario.is_valid():
            avatar = formulario.save()
            avatar.user_profile = request.user
            avatar.save()
            url_exitosa = reverse('home')
            return redirect(url_exitosa)
    else:  # GET
        formulario = AvatarFormulario()
    return render(request, "Perfiles/formulario_avatar.html", {'form': formulario})
