
# contacts/urls.py

from django.urls import path
from .views import ContactListView
from .views import ContactCreateView

urlpatterns = [
    path("create/", ContactCreateView.as_view(), name="contact_create"),
    path("", ContactListView.as_view(), name="contact_list"),
]