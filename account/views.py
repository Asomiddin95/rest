from django.shortcuts import render
from account.serializer import ContactSerilizer
from account.models import ContactModel
from rest_framework import generics


# Create your views here.

class ContactListView(generics.ListCreateAPIView):
    queryset = ContactModel.objects.all()
    serializer_class = ContactSerilizer
