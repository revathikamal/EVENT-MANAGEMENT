from django.shortcuts import render
from django.http import HttpResponse
from  clientreg.models import ClientReg

from django.conf import settings
import os
# Create your views here.
def view_client(request):
    objlist=ClientReg.objects.all()
    context={
        'objval':objlist,
    }
    return render(request, 'clientreg/viewclient.html', context)



def clientreg(request):
    if request.method=="POST":
        obj=ClientReg()

        obj.c_name=request.POST.get('cname')

        obj.c_address=request.POST.get('address')
        obj.c_email=request.POST.get('email')
        obj.c_phno=request.POST.get('mobile')
        obj.c_gender=request.POST.get('Gender')

        obj.save()

    return render(request, 'clientreg\clientreg.html')
