from django.shortcuts import render

# Create your views here.

# contacts/views.py
def start_page(request):
    return render(request, 'contacts/start_page.html', {'contacts': []})

from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Contact
from .forms import ContactForm

class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy("contact_list")

class ContactListView(ListView):
    model = Contact