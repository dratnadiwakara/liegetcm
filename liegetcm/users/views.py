from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, ArrangerForm,TCInvestorForm,TrusteeStaffForm
from django.contrib.auth.models import Group



def register(response,ut):
    if response.method=="POST":
        form = RegisterForm(response.POST)
        usertype = response.POST['usertype']
        if usertype=='arranger':
            userdataform = ArrangerForm(response.POST)
        elif usertype=='tcinvestor':
            userdataform = TCInvestorForm(response.POST)
        elif usertype=='trusteestaff':
            userdataform = TrusteeStaffForm(response.POST)

        if form.is_valid() and userdataform.is_valid():
            user=form.save()
            profile = userdataform.save(commit=False)
            profile.user = user
            profile.save()
            #### send email to activate account and reset password
            group = Group.objects.get(name=str(response.POST['usertype']))
            user.groups.add(group)
            return redirect("/login")
    else:
        usertype=ut
        form = RegisterForm()
        if usertype=='arranger':
            userdataform = ArrangerForm()
        elif usertype=='tcinvestor':
            userdataform = TCInvestorForm()
        elif usertype=='trusteestaff':
            userdataform = TrusteeStaffForm()
    
    return render(response,"users/register.html",{"form":form,"usertype":usertype,"userdataform":userdataform})
    '''if usertype=='arranger':
        return render(response,"users/register_arranger.html",{"form":form,"usertype":usertype,"userdataform":userdataform})
    elif usertype=='tcinvestor':
        return render(response,"users/register_tcinvestor.html",{"form":form,"usertype":usertype,"userdataform":userdataform})'''

