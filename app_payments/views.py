from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app_customers.models import Customer
from app_payments.models import Payment
from app_loans.models import Loan
from .serializer import PaymentSerializer, PaymentDetailSerializer
from django.shortcuts import get_object_or_404



@api_view(['POST'])
def create_payment(request):
    
    
    customer = request.data.get('customer_id')
    total_amount = request.data.get('total_amount')
    payment_request = request.data
    payment_detail = request.data.get('payment_detail')    
    loan = Loan.objects.filter()


@api_view(['GET'])
def get_payments_by_customer(request):
    customer = request.GET.get('customer_id')    
    payment = get_payments(Customer, customer)
    serializer = PaymentSerializer(payment, many=True)
    return Response(serializer.data)


def get_payments(Customer, customer_id):
    customer = get_object_or_404(Customer, external_id=customer_id)
    payments = Payment.objects.filter(customer_id=customer)
    return payments
