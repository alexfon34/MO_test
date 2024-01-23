"""MO_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_customers.views import balance, customers_list, create_customer
from app_loans.views import list_loans, create_loan, get_loans_by_customer
from app_payments.views import get_payments_by_customer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer/balance', balance, name='balance'),
    path('customer/customer_list', customers_list, name='list'),
    path('customer/create_customer', create_customer, name='create_customer'),
    path('loan/list_loans', list_loans, name='loans'),
    path('loan/create_loan', create_loan, name='create_loan'),
    path('loan/get_loans_by_customer', get_loans_by_customer, name='get_loans_by_customer'),
    path('payments/get_payments_by_customer', get_payments_by_customer, name='get_payments_by_customer')
]
