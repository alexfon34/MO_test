from django.db import models
from app_customers.models import Customer
import uuid


class Loan(models.Model):
    
    """Crea el modelo de la DB de Loans
    
    Attributes:
    created_at (DateTimeField): Fecha y hora de la creacion del préstamo
    updated_at (DateTimeField): Fecha y hora de la última actualizacion del préstamo
    external_id (UUIDField): ID único para cada préstamo
    amount (DecimalField): Monto del préstamo
    status (IntegerField): Muestra el estado del préstamo (1: Pendiente), (2: Activo), (3: Rechazado), (4: Pagado)
    contract_version (CharField): Versión del préstamo
    customer_id (ForeignKey): ID de relación con el cliente asociado 
    outstanding (DecimalField): Saldo restante
    """    
    
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
    contract_version = models.CharField(max_length=60, default='')
    customer_id = models.ForeignKey('app_customers.Customer', on_delete=models.CASCADE, to_field='external_id', null=True)
    outstanding = models.DecimalField(max_digits=12, decimal_places=2)