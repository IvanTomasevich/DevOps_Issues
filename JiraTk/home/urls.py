from django.urls import path
from .views import *


urlpatterns = [
    # path('', main_view, name='main'),
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
]
