from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreatingForm


class RegisterView(CreateView):
    form_class = CustomUserCreatingForm
    template_name = 'users/form_register.html'
    success_url = reverse_lazy('catalog:catalog_list')
