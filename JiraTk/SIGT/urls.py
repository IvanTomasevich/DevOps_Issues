from django.urls import path
from .views import \
    TicketCreateView, \
    TicketList, \
    TicketDetail, \
    TicketUpdate, \
    TicketDelete


urlpatterns = [
    path('crate-ticket/', TicketCreateView.as_view(), name='create_ticket'),
    path('list-ticket/', TicketList.as_view(), name='list_ticket'),
    path('list-ticket/<int:pk>/', TicketDetail.as_view(), name='detail_ticket'),

    path('update-ticket/<int:pk>/', TicketUpdate.as_view(), name='update_ticket'),
    path('delete-ticket/<int:pk>/', TicketDetail.as_view(), name='delete_ticket'),
]
