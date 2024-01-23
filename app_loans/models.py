from django.db import models
from app_customers.models import Customer
import uuid


class Loan(models.Model):
    
    
    status_loans_options = (        
        (1, 'Pending'),
        (2, 'Active'),
        (3, 'Rejected'),
        (4, 'Paid')
    )
    
        
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateField(auto_now=True)
    external_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.IntegerField(choices=status_loans_options, default=2)
    contract_version = models.DecimalField(max_digits=12, decimal_places=2)
    customer_id = models.ForeignKey('app_customers.Customer', on_delete=models.CASCADE, to_field='external_id', null=True)
    outstanding = models.DecimalField(max_digits=12, decimal_places=2)