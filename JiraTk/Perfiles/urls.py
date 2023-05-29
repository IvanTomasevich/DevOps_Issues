from django.urls import path
from .views import *


urlpatterns = [
    # URLS Usuario y sesion
    path('signup/', registro, name="registro"),
    path('login/', login_view, name="login"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
    # URLS de Perfil
    path('editar-mi-perfil/', MiPerfilUpdateView.as_view(), name="editar_perfil"),
    path('agregar-avatar/', agregar_avatar, name="agregar_avatar"),
]