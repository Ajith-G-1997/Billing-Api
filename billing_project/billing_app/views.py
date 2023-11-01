from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Customer, Invoice, Transaction
from .serializers import CustomerSerializer, InvoiceSerializer, TransactionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Customer, Invoice, Transaction
from .serializers import CustomerSerializer, InvoiceSerializer, TransactionSerializer,UserSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

User = get_user_model() 

class UserRegistration(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({'message': 'Registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerList(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerDetail(APIView):
    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self, request, pk):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        customer = self.get_object(pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





class InvoiceList(APIView):
    def get(self, request):
        invoices = Invoice.objects.all()
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InvoiceDetail(APIView):
    def get_object(self, pk):
        try:
            return Invoice.objects.get(pk=pk)
        except Invoice.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        invoice = self.get_object(pk)
        serializer = InvoiceSerializer(invoice)
        return Response(serializer.data)

    def put(self, request, pk):
        invoice = self.get_object(pk)
        serializer = InvoiceSerializer(invoice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        invoice = self.get_object(pk)
        invoice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TransactionList(APIView):
    def get(self, request):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TransactionDetail(APIView):
    def get_object(self, pk):
        try:
            return Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        transaction = self.get_object(pk)
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)

    def put(self, request, pk):
        transaction = self.get_object(pk)
        serializer = TransactionSerializer(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        transaction = self.get_object(pk)
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
