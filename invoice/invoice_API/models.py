from django.db import models
import uuid

# Create your models here.

# Create two Django models viz. Invoice and Invoice Detail.
# Invoice model fields -> Date, Invoice CustomerName.
# InvoiceDetail model fields -> invoice (ForeignKey), description, quantity, unit_price, price.


class Invoice(models.Model):
    invoice_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    date = models.DateField(auto_now=True)
    customer_name = models.CharField(max_length=50, null=False, blank=False)


class InvoiceDetails(models.Model):
    invoice = models.ForeignKey(Invoice, related_name="invoice", on_delete=models.CASCADE)
    desc = models.TextField()
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)