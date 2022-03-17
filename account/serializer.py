from account.models import ContactModel
from rest_framework import serializers


class ContactSerilizer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = '__all__'
