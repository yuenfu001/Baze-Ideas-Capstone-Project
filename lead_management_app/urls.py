from django.urls import path
from . import views
app_name="lead_management_app"
urlpatterns = [
    path('lead-generation/',views.lead_generation_table, name='lead_generation'),
    path('client-engagement/',views.client_engagement_table, name='client_engagement'),
    path('proposal-submission/',views.proposal_submission_table, name='proposal_submission'),
    path('quote-submission/',views.quote_submission_table, name='quote_submission'),
    path('quote-acceptance/',views.quote_acceptance_table, name='quote_acceptance'),
    path('purchase-order/',views.po_receipt_table, name='po_receipt'),
    path('payment/',views.deal_closure_table, name='deal_closure'),
]
