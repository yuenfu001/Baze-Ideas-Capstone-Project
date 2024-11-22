from django.db import models
import uuid
# Create your models here.

class ServiceRequestForm(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    client_company_name = models.CharField(max_length=100, blank=True, null=True)
    client_company_address = models.CharField(max_length=400, blank=True, null=True)
    client_coordinates = models.CharField(max_length=100, blank=True, null=True)
    client_closest_landmark = models.CharField(max_length=100, blank=True, null=True)
    client_contact_person = models.CharField(max_length=100, blank=True, null=True)
    client_designation = models.CharField(max_length=100, blank=True, null=True)
    client_department = models.CharField(max_length=100, blank=True, null=True)
    client_mobile_number = models.CharField(max_length=100, blank=True, null=True)
    client_email = models.EmailField(max_length=100, blank=True, null=True)


    srf_service_type = models.CharField(max_length=100, blank=True, null=True)
    srf_select_power = models.CharField(max_length=100, blank=True, null=True)
    srf_select_space = models.CharField(max_length=100, blank=True, null=True)
    srf_last_mile_mode_of_connection  = models.CharField(max_length=100, blank=True, null=True)
    srf_microwave_mast_availability_height = models.CharField(max_length=100, blank=True, null=True)
    srf_interface_type = models.CharField(max_length=100, blank=True, null=True)
    srf_bandwidth = models.CharField(max_length=100, blank=True, null=True)
    srf_no_of_intended_user = models.CharField(max_length=100, blank=True, null=True)

    lan_mode_of_connection = models.CharField(max_length=100, blank=True, null=True)
    lan_router_availability = models.CharField(max_length=100, blank=True, null=True)
    lan_preferred_router_type = models.CharField(max_length=100, blank=True, null=True)
    lan_switch_availability = models.CharField(max_length=100, blank=True, null=True)
    lan_preferred_switch_type = models.CharField(max_length=100, blank=True, null=True)
    lan_existing_equipment = models.CharField(max_length=100, blank=True, null=True)
    lan_rack_space_availability = models.CharField(max_length=100, blank=True, null=True)
    lan_rack_type_and_size = models.CharField(max_length=100, blank=True, null=True)
    lan_specify_others = models.CharField(max_length=100, blank=True, null=True)
    lan_supply_rack = models.CharField(max_length=100, blank=True, null=True)
    lan_power_terminal_availability = models.CharField(max_length=100, blank=True, null=True)

    vpn_mode = models.CharField(max_length=100, blank=True, null=True)
    vpn_point_a = models.CharField(max_length=100, blank=True, null=True)
    vpn_point_b = models.CharField(max_length=100, blank=True, null=True)
    vpn_vlan_tag = models.CharField(max_length=100, blank=True, null=True)
    vpn_mtu_size = models.CharField(max_length=100, blank=True, null=True)
    vpn_latency = models.CharField(max_length=100, blank=True, null=True)
    vpn_jilter = models.CharField(max_length=100, blank=True, null=True)
    vpn_p2mp_sink_location = models.CharField(max_length=100, blank=True, null=True)


    vps_no_of_virtual_machine = models.CharField(max_length=100, blank=True, null=True)
    vps_cpu_cores = models.CharField(max_length=100, blank=True, null=True)
    vps_memory_size = models.CharField(max_length=100, blank=True, null=True)
    vps_storage_size = models.CharField(max_length=100, blank=True, null=True)
    vps_operating_system = models.CharField(max_length=100, blank=True, null=True)
    vps_suite = models.CharField(max_length=100, blank=True, null=True)
    vps_other_details = models.CharField(max_length=100, blank=True, null=True)


    voice_switch_type = models.CharField(max_length=100, blank=True, null=True)
    voice_ip_phones_required = models.CharField(max_length=100, blank=True, null=True)
    voice_type_no_of_IP_phones = models.CharField(max_length=100, blank=True, null=True)
    voice_gateway_type = models.CharField(max_length=100, blank=True, null=True)
    others_other_details = models.CharField(max_length=100, blank=True, null=True)


    # validation fields
    lead_generation_status = models.BooleanField(default=False)
    client_engagment_status = models.BooleanField(default=False)
    proposal_submission_status = models.BooleanField(default=False)
    quote_submission_status = models.BooleanField(default=False)
    quote_acceptance_status = models.BooleanField(default=False)
    po_receipt_status = models.BooleanField(default=False)
    payment_status = models.BooleanField(default=False)

    # uploads
    upload_quote = models.FileField(upload_to='quote/', blank=True,null=True)
    upload_proposal = models.FileField(upload_to='proposal/', blank=True,null=True)
    upload_sla = models.FileField(upload_to='SLA/', blank=True,null=True)
    upload_receipt = models.FileField(upload_to='receipt/', blank=True,null=True)

    def __str__(self):
        return f'{self.client_company_name}'