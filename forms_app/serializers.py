from rest_framework import serializers
from .models import ServiceRequestForm

class ClientFormData(serializers.ModelSerializer):
    class Meta:
        model=ServiceRequestForm
        fields = [
            'client_contact_person','client_company_address','client_closest_landmark','client_mobile_number','client_email','srf_service_type'
        ]