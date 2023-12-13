
# contacts/urls.py

from django.urls import path

from .views import ContactListView

urlpatterns = [
    path("", ContactListView.as_view(), name="contact_list"),
]