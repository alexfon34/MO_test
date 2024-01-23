from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from app_customers.models import Customer
from django.shortcuts import get_object_or_404
from app_loans.models import Loan
from .serializer import LoanSerializer
from django.db.models import Sum


@api_view(['POST'])
def create_loan(request):
    
    """Crea nuevo prestamo a un cliente

    Returns:
        Response: Objeto con los datos del prestamo creado
    """
    
    customer_external_id = request.data.get('customer_external_id')
        
    
    #Revisa si el customer existe
    
    try:
        customer = Customer.objects.get(external_id=customer_external_id)
    except Customer.DoesNotExist:
        return Response({"error": "El customer no existe"}, status=status.HTTP_400_BAD_REQUEST)
    
    #Revisa si el customer esta activo
    
    if customer.status == 2:
        return Response({"error": "El customer no se encuentra activo"}, status=status.HTTP_400_BAD_REQUEST)
    
    #Revisa si el total_outstanding es mayor que el del customer
    
    
    loan = get_loans(Customer, customer_external_id)
    customer_outstanding = loan.aggregate(sum_outstanding=Sum('outstanding'))['sum_outstanding'] or 0
    
    if customer_outstanding >= customer.score:
        err = ('EL total del monto de los prestamos exede el límite de credito establecido')
        return Response({'error': err}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = LoanSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

@api_view(['GET'])
def list_loans(request):
        
    """Consulta la lista de todos los prestamos creados

    Returns:
        Response: Objeto con la lista de los prestamos creados
    """
    
    loan = Loan.objects.all()
    serializer = LoanSerializer(loan, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_loans_by_customer(request):
    
    """Consulta la lista de todos los prestamos creados por cliente

    Returns:
        Response: Objeto con la lista de los prestamos creados por cliente
    """
    
    customer = request.GET.get('customer_id')    
    loan = get_loans(Customer, customer)
    serializer = LoanSerializer(loan, many=True)
    return Response(serializer.data)


def get_loans(Customer, customer_id):
    customer = get_object_or_404(Customer, external_id=customer_id)
    loans = Loan.objects.filter(customer_id=customer)
    return loans
