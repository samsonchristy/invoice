from django.db import models
import decimal
# Create your models here.

class Invoice(models.Model):
    customer = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    total_quantity = models.IntegerField(default=0)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2,default=00.00)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        verbose_name_plural = "Invoice"
    
    def __str__(self):
        return self.customer

class Transaction(models.Model):
    invoice_id = models.ForeignKey(Invoice,on_delete=models.CASCADE,related_name="transactions")
    product = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    line_total = models.DecimalField(max_digits=10, decimal_places=2,editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        verbose_name_plural = "Transactions"
    
    def __str__(self):
        return self.product

    def save(self,force_insert=True, force_update=True, **kwargs):
        self.line_total = self.quantity * self.price
        super().save(*kwargs)
        invoice_obj = Invoice.objects.get(id=self.invoice_id.id)
        invoice_obj.total_quantity+=1
        invoice_obj.total_amount+=(decimal.Decimal(self.price)*decimal.Decimal(self.quantity))
        invoice_obj.save()
        
