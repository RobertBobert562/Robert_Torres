from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Contact
from .forms import ContactForm

# contacts/views.py
def start_page(request):
    return render(request, 'contacts/start_page.html', {'contacts': []})

class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm  # Replace with your actual form class
    template_name = "Robert_Torres\contacts\templates\contacts\contact_form.html"  # Replace with your actual template path
    success_url = ""  # Replace with the URL you want to redirect to after a successful form submission

class ContactListView(ListView):
    model = Contact
    template_name = "Robert_Torres\contacts\templates\contacts\contact_list.html"
    context_object_name = "contacts"
