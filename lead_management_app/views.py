from django.shortcuts import render

# Create your views here.
app_name="lead_management_app"

def lead_generation_table(request):
    title="Table"

    context = {
        'title': title
    }
    return render(request,'tables/lead_generation.html',context)

def client_engagement_table(request):
    title="Table"

    context = {
        'title': title
    }
    return render(request,'tables/client_engagement.html',context)

def proposal_submission_table(request):
    title="Table"

    context = {
        'title': title
    }
    return render(request,'tables/proposal_submission.html',context)

def quote_submission_table(request):
    title="Table"

    context = {
        'title': title
    }
    return render(request,'tables/quote_submission.html',context)

def quote_acceptance_table(request):
    title="Table"

    context = {
        'title': title
    }
    return render(request,'tables/quote_acceptance.html',context)

def po_receipt_table(request):
    title="Table"

    context = {
        'title': title
    }
    return render(request,'tables/quote_submission.html',context)

def deal_closure_table(request):
    title="Table"

    context = {
        'title': title
    }
    return render(request,'tables/deal_closure.html',context)