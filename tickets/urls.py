from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import TicketList, TicketCreate


urlpatterns = [
    path('', login_required(TicketList.as_view()), name='ticket_list'),
    path('create/', login_required(TicketCreate.as_view()), name='ticket_create'),
]
