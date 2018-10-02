from django.views.generic import CreateView
from django.contrib.auth import login, authenticate
from .forms import RegisterForm


class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = '/tickets/'

    def form_valid(self, form):
        valid = super(RegisterView, self).form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid