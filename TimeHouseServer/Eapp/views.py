from django.shortcuts import render

# Create your views here.

def appDes(request):
    return render(request, 'Eapp/webapp.html')