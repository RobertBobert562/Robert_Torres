from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Contact
from .forms import ContactForm

# contacts/views.py

class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = "contacts/contact_create.html"
    success_url = '/contacts/contact_list/'

    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect(self.success_url)

class ContactListView(ListView):
    model = Contact
    template_name = "contacts/contact_list.html"
    context_object_name = "contacts"

class ContactEditView(UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = "contacts/contact_edit.html" 
    success_url = '/contacts/contact_list/'

class ContactDeleteView(DeleteView):
    model = Contact
    template_name = "contacts/contact_confirm_delete.html" 
    success_url = '/contacts/contact_list/'  

class ContactDetailView(DetailView):
    model = Contact
    template_name = "contacts/contact_detail.html"
    context_object_name = "contact"