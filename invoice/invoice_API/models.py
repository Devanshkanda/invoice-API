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

    def __str__(self) -> str:
        return f"{self.customer_name} id : {self.invoice_id}"


class InvoiceDetails(models.Model):
    invoice = models.ForeignKey(Invoice, related_name="invoice", on_delete=models.CASCADE)
    desc = models.TextField()
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=5, decimal_places=2)


    @property
    def price(self):
        return self.quantity * self.unit_price
    
    @price.setter
    def price(self):
        raise AttributeError("Price cannot be set, it is a calculated field")