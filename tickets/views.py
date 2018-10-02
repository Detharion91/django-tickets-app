from django.views import generic
from .models import Ticket
from .forms import TicketForm


class TicketList(generic.ListView):
    model = Ticket
    paginate_by = 20
    context_object_name = 'ticket_list'
    template_name = 'tickets/ticket_list.html'

    def get_queryset(self):
        tickets = Ticket.objects.filter(owner=self.request.user).order_by('created_date')
        return tickets


class TicketCreate(generic.CreateView):
    template_name = 'tickets/ticket_create.html'
    form_class = TicketForm
    success_url = '/tickets/'

    def form_valid(self, form):
        ticket = form.save(commit=False)
        ticket.owner = self.request.user
        return super(TicketCreate, self).form_valid(form)