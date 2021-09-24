from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Invoice,Transaction
from .serializers import InvoiceSerializer,TransactionSerializer
from rest_framework import status
from rest_framework import viewsets

# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def invoices(request,pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            try:
                inv = Invoice.objects.get(id=id)
                serializer = InvoiceSerializer(inv)
                return Response(serializer.data,status=status.HTTP_200_OK)
            except:
                return Response({'failed':'No data available'},status=status.HTTP_400_BAD_REQUEST)
        inv = Invoice.objects.all()
        serializer = InvoiceSerializer(inv, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    if request.method == 'POST':
        try:
            invoice_obj=Invoice.objects.create(customer=request.data['customer'])
            for trans in request.data['transactions']:
                total = trans['product'] * trans['quantity']
                Transaction.objects.create(invoice_id=invoice_obj,product=trans['product'],quantity=trans['quantity'],price=trans['price'],line_total=total)
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        except:
            return Response({'msg':'Data not created'},status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        id = pk
        try:
            invoice_obj = Invoice.objects.get(pk=id)
        except:
            return Response({'msg':'Data with the id not present'},status=status.HTTP_400_BAD_REQUEST)
        else:
            for trans in request.data['transactions']:
                total = trans['product'] * trans['quantity']
                Transaction.objects.create(invoice_id=invoice_obj,product=trans['product'],quantity=trans['quantity'],price=trans['price'],line_total=total)
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
    
    if request.method == 'DELETE':
        id = pk
        try:
            stu = Invoice.objects.get(pk=id)
            stu.delete()
            return Response({'msg':'Data Deleted'},status=status.HTTP_200_OK)
        except:
            return Response({'failed':'No data available'},status=status.HTTP_400_BAD_REQUEST)


# for post
{
    "customer": "samson",
    "transactions": [
        { 
        "product": "oven",
        "quantity": 5,
        "price": 30.00
        },
        { 
        "product": "heater",
        "quantity": 10,
        "price": 25.00
        },
        { 
        "product": "tv",
        "quantity": 2,
        "price": 45.00
        }
    ]
}


#for put
{
    "id": 53,
    "customer": "test",
    "transactions": [
        {
        "product": "test prod",
        "quantity": 2,
        "price": 10.00
        },
        {
        "product": "test prod",
        "quantity": 1,
        "price": 10.00
        }
    ]
}