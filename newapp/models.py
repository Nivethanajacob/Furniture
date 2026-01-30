from django.db import models

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    product = models.CharField(max_length=50)
    quantity = models.IntegerField()
    address = models.TextField()
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.customer_name} - {self.product}"

