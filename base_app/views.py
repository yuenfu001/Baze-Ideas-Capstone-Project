from django.shortcuts import render

# Create your views here.

def home(request):
    title="Dashboard"

    context={
        'title':title
    }
    return render(request,'base/index.html',context)  