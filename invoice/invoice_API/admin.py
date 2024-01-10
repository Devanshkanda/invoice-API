from django.contrib import admin
from .models import *
# Register your models here.


class invoiceAdmin(admin.ModelAdmin):
    list_display = ("invoice_id", "customer_name", "date")


class invoiceDetailAdmin(admin.ModelAdmin):
    list_display = ("invoice", "desc")


admin.site.register(Invoice, invoiceAdmin)
admin.site.register(InvoiceDetails, invoiceDetailAdmin)
