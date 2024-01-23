from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import CustomerSerializer
from .models import Customer
from django.shortcuts import get_object_or_404
from app_loans.models import Loan
from django.db.models import Sum



@api_view(['GET'])
def balance(request):
    customer_id = request.GET.get('customer_id')
    customer = get_object_or_404(Customer, external_id=customer_id)
    print('cliente', customer.score)

    if not customer:
        return Response({"error": "A 'customer' parameter is required."},
                        status=status.HTTP_400_BAD_REQUEST)
    # Calcular total deuda
    print(customer_id)
    loans = Loan.objects.filter(customer_id=customer_id, status=2)
    print('loans', loans)
    total_debt = loans \
        .aggregate(sum_outstanding=Sum('outstanding'))['sum_outstanding']
    
    # Calcular monto disponible
    print('score', customer.score, total_debt)
    available_amount = customer.score - total_debt
    
    return Response({
        "total_debt": total_debt,
        "available_amount": available_amount
    })

    


@api_view(['POST'])
def create_customer(request):
    serializer = CustomerSerializer(data=request.data)        
    print('respuesta', serializer)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def customers_list(request):        
    customer = Customer.objects.all()
    serializer = CustomerSerializer(customer, many=True)
    return Response(serializer.data)