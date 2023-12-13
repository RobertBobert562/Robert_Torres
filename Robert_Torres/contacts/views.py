from django.shortcuts import render

# Create your views here.

# contacts/views.py
def start_page(request):
    return render(request, 'contacts/start_page.html', {'contacts': []})


from django.views.generic import ListView

from .models import Contact


class ContactListView(ListView):
    model = Contact