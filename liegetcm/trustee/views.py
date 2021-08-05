from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.models import Group


def is_arranger(user):
    return user.groups.filter(name="arranger").exists() 

def is_tcinvestor(user):
    return user.groups.filter(name="tcinvestor").exists() 


def index(request):
    return HttpResponse("Trustee Home page")


@login_required(login_url="/login/")
def home(request):
    if is_arranger(request.user):
        return render(request,"trustee/arranger_home.html")
    elif is_tcinvestor(request.user):
        return render(request,"trustee/tcinvestor_home.html")
    else:
        return redirect('/login')