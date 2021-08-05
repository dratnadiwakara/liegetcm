from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    legal_name = models.CharField(max_length=200,null=True)
    contact_name = models.CharField(max_length=200,null=True)
    phone_number = models.PositiveIntegerField(null=True)
    company_registration_number = models.CharField(max_length=200,null=True)
    vat_no = models.CharField(max_length=200,null=True)
    address = models.CharField(max_length=200,null=True)
    bank_account_number = models.PositiveIntegerField(null=True)
    bank_name = models.CharField(max_length=50,null=True)
    bank_branch = models.CharField(max_length=50,null=True)
    nic_number = models.CharField(max_length=15,null=True)

