from django.db import models

class Customers(models.Model):
    customer_id = models.CharField(primary_key=True, max_length=20)
    company_name = models.CharField(max_length=40)
    contact_name = models.CharField(max_length=30, blank=True, null=True)
    contact_title = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=60, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    region = models.CharField(max_length=15, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=15, blank=True, null=True)
    phone = models.CharField(max_length=24, blank=True, null=True)
    fax = models.CharField(max_length=24, blank=True, null=True)

    def __str__(self):
        return f"{self.company_name}, {self.contact_name}, {self.city}, {self.country}"

    class Meta:
        managed = False
        db_table = 'customers'
        ordering = ("company_name", "contact_name", "city", "country")
