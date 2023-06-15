from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.shortcuts import render, redirect
from .forms import CreateTicket
from .models import Ticket

# Create your views here.


class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    form_class = CreateTicket
    template_name = 'formulario_ticket.html'
    success_url = 'home'

