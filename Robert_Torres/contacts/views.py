from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Contact
from .forms import ContactForm

# contacts/views.py
def start_page(request):
    return render(request, 'contact_list.html')

class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm  # Replace with your actual form class
    template_name = "contacts/contact_create.html"  # Replace with your actual template path
    success_url = reverse_lazy('contact_list')  # Replace with the URL you want to redirect to after a successful form submission

    def form_valid(self, form):
        # Additional validation logic can be added here
        return super().form_valid(form)

class ContactListView(ListView):
    model = Contact
    template_name = "Robert_Torres\contacts\templates\contacts\contact_list.html"
    context_object_name = "contacts"
