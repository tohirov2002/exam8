from rest_framework import serializers
from .models import ContactsModel  # Assuming your models.py is in the same directory


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactsModel
        fields = '__all__'

