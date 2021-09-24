from django.db import models
from django.db.models import fields
from .models import Invoice, Transaction
from rest_framework import serializers


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id','product','quantity','price','line_total']

class InvoiceSerializer(serializers.ModelSerializer):
    transactions = TransactionSerializer(read_only=False,many=True)
    class Meta:
        model = Invoice
        fields = ['id','customer','date','total_quantity','total_amount','transactions']
