from django.db import models
from operators.models import Operator

class Booking(models.Model):
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    number_of_guests = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    option_until = models.DateField()
    confirmed_at = models.DateField(blank=True, null=True)
    cancelation_terms = models.TextField()
    payment_terms = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking {self.id} - {self.operator.name}"