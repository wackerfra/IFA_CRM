from django.db import models
from operators.models import Operator, Hotel
from django.contrib.auth.models import User
from django.conf import settings



class Booking(models.Model):
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)  # Link to the Hotel model
    double_rooms = models.IntegerField(default=0)  # Number of double rooms requested
    single_rooms = models.IntegerField(default=0)  # Number of single rooms requested
    segment = models.IntegerField(choices=Operator.SEGMENT_CHOICES, default=7)  # Choices from Operator model

    check_in = models.DateField()
    check_out = models.DateField()
    number_of_guests = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    option_until = models.DateField()
    confirmed_at = models.DateField(blank=True, null=True)
    cancelation_terms = models.TextField()
    payment_terms = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    sales_representative = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Link to Django's User model
        on_delete=models.CASCADE,  # Delete bookings if the user is deleted
        related_name='bookings',  # Optional related name for reverse lookup
    )

    def __str__(self):
        return f"Booking: {self.operator.name} - {self.hotel.name} by {self.sales_representative.username}"
