
# contacts/urls.py

from django.urls import path
from . import views
from .views import ContactListView, ContactCreateView

app_name = 'contacts'

urlpatterns = [
    path('', ContactListView.as_view(), name='contact_list'),
    path("contact_create/", views.ContactCreateView.as_view(), name="contact_create"),
    path("contact_form/", views.ContactListView.as_view(), name='contact_list'),
]