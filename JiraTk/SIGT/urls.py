from django.urls import path
from .views import *


urlpatterns = [
    path('sigt/', sigt_view, name='sigt'),
]
