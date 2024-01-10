from rest_framework import serializers
from .models import *


class InvoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invoice
        fields = ['customer_name', 'date']
        
    

    def validate(self, validated_data):
        customer_name: str = validated_data.get('customer_name')

        if customer_name is None:
            raise serializers.ValidationError("customer name not entered")

        if len(customer_name) < 2 and len(customer_name) > 20:
            raise serializers.ValidationError("invalid name")
        
        return validated_data
    

    def create(self, validated_data):
        try:
            invoice_obj = Invoice.objects.create(
                customer_name=str(validated_data.get('customer_name'))
            )

            invoice_obj.save()
            return invoice_obj
        
        except Exception as e:
            print(e)
            raise serializers.ValidationError("error")
        
    
    def update(self, instance, validated_date):
        instance.customer_name = validated_date.get('customer_name')
        instance.save()
        return instance


class InvoiceDetailSerializer(serializers.ModelSerializer):

    # invoice_customer_detail = InvoiceSerializer()

    class Meta:
        model = InvoiceDetails
        fields = ['invoice', 'desc', 'quantity', 'unit_price', 'price']

    
    def validate(self, validated_data):
        print("i am in validate fucn of invoice detail serializer")
        print(validated_data)

        desc: str = validated_data.get('desc')
        quantity: int = validated_data.get('quantity')
        unit_price: float = validated_data.get('unit_price')
        
        if desc is None:
            raise serializers.ValidationError("Description not entered")
        
        if quantity is None:
            raise serializers.ValidationError("quantity not entered")
        
        if unit_price is None:
            raise serializers.ValidationError("unit price not entered")
        
        if quantity < 0 or quantity > 10000:
            raise serializers.ValidationError("Invalid quantity entered")
        
        if unit_price < 0:
            raise serializers.ValidationError("Invaid unit price entered")
        
        return validated_data
    


    def create(self, validated_data):
        try:
            print("i am in create fucn of invoice detail serializer")
            print(validated_data)

            invoice_detail_obj = InvoiceDetails.objects.create(
                invoice = validated_data.get('invoice'),
                desc = str(validated_data.get('desc')),
                quantity = int(validated_data.get('quantity')),
                unit_price = validated_data.get('unit_price'),
            )

            invoice_detail_obj.save()
            return invoice_detail_obj

        except Exception as e:
            print(e)
    

    def update(self, instance, validated_data):
        instance.desc = validated_data.get('desc')
        instance.quantity = validated_data.get('quantity')
        instance.unit_price = validated_data.get('unit_price')

        instance.save()
        return instance