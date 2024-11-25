from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.


@login_required(login_url='/')
def home(request):
    title="Dashboard"

    context={
        'title':title
    }
    return render(request,'base/index.html',context)