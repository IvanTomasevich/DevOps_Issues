from django.urls import path
from .views import TicketCreateView


urlpatterns = [
    path('crate-ticket/', TicketCreateView.as_view(), name='create_ticket'),
]
