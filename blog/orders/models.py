from django.db import models
from django.contrib.auth.models import User
from enumfields.fields import EnumField
from orders.enums import OrderStatus


class Order(models.Model):
    number = models.CharField(max_length=12)
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
    status = EnumField(OrderStatus, default=OrderStatus.shipped)
    amount = models.IntegerField()
    date_start = models.DateField()
    date_end = models.DateField()

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ('date_end',)
