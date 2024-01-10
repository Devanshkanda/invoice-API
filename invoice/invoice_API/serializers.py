from rest_framework import serializers
from .models import *

class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetails
        fields = '__all__'
    

    def validate(self, validated_data):
        pass


    def create(self, validated_data):
        
        pass


class InvoiceSerializer(serializers.ModelSerializer):

    invoice_details = InvoiceDetailSerializer()

    class Meta:
        model = Invoice
        fields = '__all__'
    

    def validate(self, validated_data):
        customer_name: str = validated_data.get('customer_name')
        desc: str = validated_data.get('desc')
        quantity: int = validated_data.get('quantity')
        unit_price: int = validated_data.get('unit_price')
        price: int = validated_data.get('price')

        if len(customer_name) < 2 and len(customer_name) > 20:
            raise serializers.ValidationError("invalid name")
        
        if quantity < 0 or quantity > 10000:
            raise serializers.ValidationError("Invalid quantity entered")
        
        if unit_price < 0:
            raise serializers.ValidationError("Invaid unit price entered")
        
        if price < 0:
            raise serializers.ValidationError("Invalid price entered")
        
        return validated_data
    

    def create(self, validated_data):
        try:
            invoice_obj = Invoice.objects.create(customer_name=str(validated_data.get('customer_name')))

            invoice_detail_obj = InvoiceDetails.objects.create(
                invoice = invoice_obj.invoice_id,
                desc = validated_data.get('desc'),
                quantity = validated_data.get('quantity'),
                unit_price = validated_data.get('unit_price'),
                price = validated_data.get('price')
            )

            invoice_obj.save()
            invoice_detail_obj.save()

            return invoice_detail_obj

        except Exception as e:
            print(e)