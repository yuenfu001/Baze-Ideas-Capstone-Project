from django.contrib import admin
from .models import ServiceRequestForm
# Register your models here.

@admin.register(ServiceRequestForm)
class srfAdmin(admin.ModelAdmin):
    list_display = [
                    'client_company_name','client_company_address','srf_service_type'
                    ]
