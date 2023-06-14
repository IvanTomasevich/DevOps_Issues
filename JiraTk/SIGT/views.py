from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

# Create your views here.


def sigt_view(request):
    return render(request, "sigt.html", {})


