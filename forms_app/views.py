from django.shortcuts import render

# Create your views here.
def lead_creation(request):
    title="Lead Creation"

    context={
        'title':title
    }

    return render(request,'forms/lead_creation.html', context)