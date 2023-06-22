from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from . import forms
from .models import Ticket
from .forms import CreateTicket
# from django.contrib.auth.decorators import login_required

# Create your views here.


class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    form_class = CreateTicket
    template_name = 'formulario_ticket.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user  # Asigna el usuario logueado al campo ForeignKey 'author'
        return super().form_valid(form)


class TicketList(ListView):
    model = Ticket
    template_name = 'list_tickets.html'


class TicketDetail(DetailView):
    model = Ticket
    success_url = reverse_lazy('list_tickets')
