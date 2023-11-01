from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from .models import Customer, Invoice, Transaction
from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = get_user_model()  
        fields = ['id', 'name', 'email', 'password']  

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = get_user_model().objects.create_user(**validated_data)
        user.set_password(password)  # Set and hash the password
        user.save()

        return user






      
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
