from django.urls import path
from .views import CustomerList, CustomerDetail, InvoiceList,UserRegistration, InvoiceDetail, TransactionList, TransactionDetail

urlpatterns = [
    path('register/',UserRegistration.as_view(),name='register'),
    path('customers/', CustomerList.as_view(), name='customer-list'),
    path('customers/<int:pk>/', CustomerDetail.as_view(), name='customer-detail'),
    path('invoices/', InvoiceList.as_view(), name='invoice-list'),
    path('invoices/<int:pk>/', InvoiceDetail.as_view(), name='invoice-detail'),
    path('transactions/', TransactionList.as_view(), name='transaction-list'),
    path('transactions/<int:pk>/', TransactionDetail.as_view(), name='transaction-detail'),
]
