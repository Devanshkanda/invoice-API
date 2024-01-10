from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.db.models import Q
import uuid
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
# Create your views here.

class InvoiceViewSet(viewsets.ModelViewSet):

    queryset = InvoiceDetails.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.AllowAny]
    # http_method_names = ['get', 'post', 'head', 'delete', 'put', 'patch']


    @method_decorator(cache_page(60 * 60))
    def list(self, request):
        try:
            print("i am in list func")
            queryset = InvoiceDetails.objects.all()
            serialize = InvoiceDetailSerializer(queryset, many=True)

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

            # invoice model serializer
            serialize = InvoiceSerializer(data=data)

            if serialize.is_valid():
                invoice_obj = serialize.save()

                data['invoice'] = invoice_obj.invoice_id
                print(data['invoice'])
                print(data)

                # invoice detail model serializer
                invoice_Detail_serialize = InvoiceDetailSerializer(data=data)

                if invoice_Detail_serialize.is_valid():
                    invoice_Detail_serialize.save()

                    return Response({
                        'status': 201,
                        'message': "Invoice Created successfully",
                        'invoice customer detail': serialize.data,
                        'date': invoice_Detail_serialize.data
                    }, status=status.HTTP_201_CREATED)
                
                return Response({
                    'status': 400,
                    'message': "error occured",
                    'error': invoice_Detail_serialize.errors
                }, status=status.HTTP_400_BAD_REQUEST)
            
            return Response({
                    'status': 400,
                    'message': "error occured",
                    'error': serialize.errors
                }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(e)
        
        return Response({
            'status': 400,
            'error': "Something went wrong"
        }, status=status.HTTP_400_BAD_REQUEST)
    


    def retrieve(self, request, pk):
        try:
            print("i am in retrive func", pk)

            invoice_obj = Invoice.objects.filter(invoice_id = uuid.UUID(pk)).first()

            if invoice_obj is None:
                return Response({
                    'status': 404,
                    'message': "Invoice not found",
                }, status=status.HTTP_404_NOT_FOUND)
            
            invoice_Details_objs = InvoiceDetails.objects.filter(invoice = invoice_obj.invoice_id)

            serialize = InvoiceDetailSerializer(invoice_Details_objs.first())

            return Response({
                'status': 200,
                'message': "invoice fetched successfully",
                'data': serialize.data
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            print(e)
        
        return Response({
            'status': 400,
            'error': "Something went wrong"
        }, status=status.HTTP_400_BAD_REQUEST)
    


    def update(self, request):
        try:

            data = request.data
            customer_objs = Invoice.objects.filter(
                Q(invoice_id = uuid.UUID(data.get('invoice'))) | 
                Q(customer_name=str(data.get('customer_name')))
            )

            if customer_objs.count() == 0:
                return Response({
                    'status': 404,
                    'message': "Sorry no user exists",
                }, status=status.HTTP_404_NOT_FOUND)
            
            # invoice model serializer
            serialize = InvoiceSerializer(customer_objs.first(), data=data)

            if serialize.is_valid():
                invoice_obj = serialize.save()

                invoice_detail_obj = InvoiceDetails.objects.filter(invoice = invoice_obj.invoice_id).first()
                
                 # invoice detail model serializer
                invoice_detail_serialize = InvoiceDetailSerializer(invoice_detail_obj, data=data)

                if invoice_detail_serialize.is_valid():
                    return Response({
                        'status': 200,
                        'message': "Invoice Updated successfully",
                        'date': serialize.data
                    }, status=status.HTTP_201_CREATED)
                
                return Response({
                    'status': 400,
                    'message': "error occured",
                    'error': invoice_detail_serialize.errors
                })
            
            return Response({
                    'status': 400,
                    'message': "error occured",
                    'error': serialize.errors
                })
            
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
    


    def destroy(self, request, pk):
        try:
            invoice_id = uuid.UUID(pk)
            invoice_obj = Invoice.objects.filter(invoice_id = invoice_id)

            if not invoice_obj.exists() or invoice_obj.count() == 0:
                return Response({
                    'status': 404,
                    'message': "Invoice does not exist",
                }, status=status.HTTP_404_NOT_FOUND)
            
            invoice_obj[0].delete()

            return Response({
                'status': 204,
                'message': "Invoice Deleted Successfully"
            }, status=status.HTTP_204_NO_CONTENT)
        
        except Exception as e:
            print(e)
        
        return Response({
            'status': 400,
            'error': "Something went wrong"
        }, status=status.HTTP_400_BAD_REQUEST)