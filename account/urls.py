from django.urls import path
from account.views import ContactListView

urlpatterns = [
    path('contact-list/',ContactListView.as_view()),
]
