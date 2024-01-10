from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.db.models import Q
# Create your views here.

class InvoiceViewSet(viewsets.ModelViewSet):

    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        try:
            serialize = InvoiceSerializer(self.queryset, many=True)

            if serialize.is_valid():
                return Response({
                    'status': 200,
                    'message': "fetched all invoices and its details",
                    'date': serialize.data
                }, status=status.HTTP_200_OK)
            
            return Response({
                'status': 400,
                'error': "error occured"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            print(e)

        return Response({
            'status': 400,
            'error': "Something went wrong"
        }, status=status.HTTP_400_BAD_REQUEST)
    


    def create(self, request):
        try:
            data = request.data

            serialize = InvoiceSerializer(data=data)

            if serialize.is_valid():
                serialize.save()

                return Response({
                    'status': 201,
                    'message': "Invoice Created successfully",
                    'date': serialize.data
                }, status=status.HTTP_201_CREATED)

        except Exception as e:
            print(e)
        
        return Response({
            'status': 400,
            'error': "Something went wrong"
        }, status=status.HTTP_400_BAD_REQUEST)
    

    def retrieve(self, request):
        try:
            pass
        except Exception as e:
            print(e)
    

    def update(self, request):
        try:

            data = request.data
            customer_obj = Invoice.objects.filter(
                Q(invoice_id=data.get('invoice')) | 
                Q(customer_name=str(data.get('customer_name')))
            )

            if customer_obj.count() == 0:
                return Response({
                    'status': 404,
                    'message': "Sorry no user exists",
                }, status=status.HTTP_404_NOT_FOUND)
            

            serialize = InvoiceSerializer(customer_obj, data=data)

            if serialize.is_valid():
                serialize.save()

                return Response({
                    'status': 200,
                    'message': "Invoice Updated successfully",
                    'date': serialize.data
                }, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            print(e)
        
        return Response({
            'status': 400,
            'error': "Something went wrong"
        }, status=status.HTTP_400_BAD_REQUEST)
    

    def partial_update(self, request):
        try:

            pass
        
        except Exception as e:
            print(e)
        
        return Response({
            'status': 400,
            'error': "Something went wrong"
        }, status=status.HTTP_400_BAD_REQUEST)
    


    def destroy(self, request):
        try:
            data = request.data

            invoice_id = data.get('invoice_id')

            invoice_obj = Invoice.objects.filter(invoice_id=invoice_id)

            if not invoice_obj.exists() or invoice_obj.count() == 0:
                return Response({
                    'status': 404,
                    'message': "Invoice does not exist",
                }, status=status.HTTP_404_NOT_FOUND)
            
            invoice_obj.delete()

            return Response({
                'status': 200,
                'message': "Invoice Deleted Successfully"
            }, status=status.HTTP_200_OK)
        

        except Exception as e:
            print(e)
        
        return Response({
            'status': 400,
            'error': "Something went wrong"
        }, status=status.HTTP_400_BAD_REQUEST)