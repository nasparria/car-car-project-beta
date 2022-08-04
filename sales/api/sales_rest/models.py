from django.db import models
from django.urls import reverse


class AutomobileVO(models.Model):
    import_href = models.CharField(max_length=200, unique=True)
    vin = models.CharField(max_length=17, unique=True) 
    is_sold = models.BooleanField(default=False)


class SalesPerson(models.Model):
    name = models.CharField(max_length=200)
    employee_number = models.PositiveIntegerField(unique=True)

    def get_api_url(self):
        return reverse("api_sales_person", kwargs={"employee_number": self.id})


class Customer(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=12)

    def get_api_url(self):
        return reverse("api_customer", kwargs={"pk": self.id})


class SaleRecord(models.Model):
    price = models.PositiveIntegerField()

    automobile = models.ForeignKey(
        AutomobileVO,
        related_name="automobile",
        on_delete=models.PROTECT,
    )

    customer = models.ForeignKey(
        Customer,
        related_name="customer",
        on_delete=models.CASCADE,
    )

    sales_person = models.ForeignKey(
        SalesPerson,
        related_name="+",
        on_delete=models.CASCADE,
    )

    def get_api_url(self):
        return reverse("api_sale_record", kwargs={"pk": self.id})