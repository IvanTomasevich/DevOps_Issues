from django.urls import path
from .views import \
    TicketCreateView, \
    TicketList, \
    TicketDetail


urlpatterns = [
    path('crate-ticket/', TicketCreateView.as_view(), name='create_ticket'),
    path('list-ticket/', TicketList.as_view(), name='list_ticket'),
    path('list-ticket/<int:pk>/', TicketDetail.as_view(), name='detail_ticket')
]
