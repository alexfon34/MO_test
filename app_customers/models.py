from django.db import models
import uuid


class Customer(models.Model):
    
    """Crea el modelo de la DB de customers
    
    Attributes:
    created_at (DateTimeField): Fecha y hora de la creacion del cliente
    updated_at (DateTimeField): Fecha y hora de la última actualizacion del cliente
    external_id (UUIDField): ID único para cada cliente
    status (IntegerField): Muestra si el cliente está activo o no (1: Activo), (2: Activo)
    score (IntegerField): Puntaje otorgado al cliente
    """
    
    
    
    status_customer_options = (
        (1, 'Activo'),
        (2, 'Inctivo')
    )
    
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    external_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    status = models.IntegerField(choices=status_customer_options)
    score = models.DecimalField(max_digits=12, decimal_places=2)