from users.models import Profile
from django import forms
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField( )

    class Meta:
        model = User
        fields = ['username','password1','password2','email']


class ArrangerForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('legal_name', 'contact_name', 'phone_number','company_registration_number','vat_no','address')

class TCInvestorForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('legal_name', 'contact_name', 'phone_number','address','nic_number','bank_account_number','bank_name','bank_branch')

