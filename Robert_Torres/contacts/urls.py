# contacts/urls.py

from django.urls import path
from . import views
from .views import ContactListView, ContactCreateView, ContactDeleteView, ContactEditView
app_name = 'contacts'

urlpatterns = [
    path('contact_list/', views.ContactListView.as_view(), name='contact_list'),
    path('contact_create/', views.ContactCreateView.as_view(), name='contact_create'),
    path('contact_edit/<int:pk>/', views.ContactEditView.as_view(), name='contact_edit'),
    path('contact_confirm_delete/<int:pk>/', views.ContactDeleteView.as_view(), name='contact_confirm_delete'),
    path('contact_detail/<int:pk>/', views.ContactDetailView.as_view(), name='contact_detail'),
]