from django.db import models
from app_loans.models import Loan
import uuid

class Payment(models.Model):   
     
    
    status_payment_options = (        
        (1, 'Completed'),
        (2, 'Rejected')
    )    
    
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateField(auto_now=True)
    external_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    total_amount = models.DecimalField(max_digits=20, decimal_places=10)
    status = models.IntegerField(choices=status_payment_options)
    
    
class PaymentDetail(models.Model):
    
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateField(auto_now=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    loan_id = models.ForeignKey(Loan, to_field='external_id', on_delete=models.CASCADE, related_name='loan_id', null=True)
    payment_id = models.ForeignKey(Payment, to_field='external_id', on_delete=models.CASCADE, related_name='payment_id')    