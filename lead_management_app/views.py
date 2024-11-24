from django.shortcuts import render
from forms_app.models import ServiceRequestForm

# Create your views here.
app_name = "lead_management_app"


def lead_generation_table(request):
    title = "Table"
    lead = ServiceRequestForm.objects.filter(lead_generation_status=True)
    context = {"title": title, "lead": lead}
    return render(request, "tables/lead_generation.html", context)


def client_engagement_table(request):
    title = "Table"
    client_engage = ServiceRequestForm.objects.filter(
        lead_generation_status=True, client_engagement_status=True
    )
    context = {"title": title, "client_engage_table": client_engage}
    return render(request, "tables/client_engagement.html", context)


def proposal_submission_table(request):
    title = "Table"
    p_submission = ServiceRequestForm.objects.filter(
        lead_generation_status=True,
        client_engagement_status=True,
        proposal_submission_status=True,
    )
    context = {"title": title, "proposal": p_submission}
    return render(request, "tables/proposal_submission.html", context)


def quote_submission_table(request):
    title = "Table"

    q_submission = ServiceRequestForm.objects.filter(
        lead_generation_status=True,
        client_engagement_status=True,
        proposal_submission_status=True,
        quote_submission_status=True,
    )

    context = {"title": title, "quote_submit": q_submission}
    return render(request, "tables/quote_submission.html", context)


def quote_acceptance_table(request):
    title = "Table"

    q_acceptance = ServiceRequestForm.objects.filter(
        lead_generation_status=True,
        client_engagement_status=True,
        proposal_submission_status=True,
        quote_submission_status=True,
        quote_acceptance_status=True,
    )
    context = {"title": title, "quote_accept": q_acceptance}
    return render(request, "tables/quote_acceptance.html", context)


def po_receipt_table(request):
    title = "Table"
    po_receipt = ServiceRequestForm.objects.filter(
        lead_generation_status=True,
        client_engagement_status=True,
        proposal_submission_status=True,
        quote_submission_status=True,
        quote_acceptance_status=True,
        po_receipt_status=True,
    )

    context = {"title": title, "receipt": po_receipt}
    return render(request, "tables/quote_submission.html", context)


def deal_closure_table(request):
    title = "Table"
    closure = ServiceRequestForm.objects.filter(
        lead_generation_status=True,
        client_engagement_status=True,
        proposal_submission_status=True,
        quote_submission_status=True,
        quote_acceptance_status=True,
        po_receipt_status=True,
        payment_status=True,
    )

    context = {"title": title}
    return render(request, "tables/deal_closure.html", context)
