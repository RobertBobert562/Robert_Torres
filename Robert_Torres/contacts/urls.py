
# contacts/urls.py

from django.urls import path
from . import views
from .views import ContactListView, ContactCreateView

app_name = 'contacts'

urlpatterns = [
    path("", views.ContactListView.as_view(), name='contact_list'),
    path("create/", views.ContactCreateView.as_view(), name="contact_create"),
]