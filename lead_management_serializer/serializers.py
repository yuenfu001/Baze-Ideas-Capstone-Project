from rest_framework import serializers
from forms_app.models import ServiceRequestForm

class ClientFormDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=ServiceRequestForm
        fields = [
            'client_contact_person','client_company_address','client_closest_landmark','client_mobile_number','client_email','srf_service_type'
        ]