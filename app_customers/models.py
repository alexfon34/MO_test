from django.db import models
import uuid


class Customer(models.Model):
    
    
    status_customer_options = (
        (1, 'Activo'),
        (2, 'Inctivo')
    )
    
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    external_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    status = models.IntegerField(choices=status_customer_options)
    score = models.DecimalField(max_digits=12, decimal_places=2)