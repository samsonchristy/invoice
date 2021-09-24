from django.contrib import admin
from .models import *
from django.contrib.auth.models import User, Group
# Register your models here.

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display=['customer','date','total_quantity','total_amount']

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display=['product','quantity','price','line_total','invoice_id']

admin.site.unregister(User)
admin.site.unregister(Group)