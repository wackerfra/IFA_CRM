from django.contrib.auth.models import User
from django.db import models
from datetime import date
from operators.models import Operator
from operators.models import Hotel
from django.utils.timezone import now
from django.conf import settings

class HotelSeason(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="seasons")
    name = models.CharField(max_length=50, help_text="Name of the season, e.g., Summer, Winter, etc.")
    start_date = models.DateField(help_text="The start date of the season.")
    end_date = models.DateField(help_text="The end date of the season.")

    class Meta:
        # Prevent overlapping seasons for the same hotel
        unique_together = ('hotel', 'name')

    def clean(self):
        """
        Ensure that the start_date and end_date do not overlap with other seasons of the same hotel.
        """
        from django.core.exceptions import ValidationError
        conflicts = HotelSeason.objects.filter(
            hotel=self.hotel,
            start_date__lte=self.end_date,
            end_date__gte=self.start_date
        ).exclude(pk=self.pk)
        if conflicts.exists():
            raise ValidationError("Season dates overlap with an existing season for this hotel.")

    def __str__(self):
        return f"{self.name} ({self.start_date} to {self.end_date}) - {self.hotel.name}"


# HotelSeasonPricing Model
class HotelSeasonPricing(models.Model):
    season = models.ForeignKey(HotelSeason, on_delete=models.CASCADE, related_name="price_details")
    room_type = models.CharField(max_length=50, help_text="Room type, e.g., Single, Double, Suite, etc.")
    base_price = models.DecimalField(max_digits=10, decimal_places=2,
                                     help_text="Base price for the room during the season.")
    weekend_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,
                                        help_text="Weekend price for the room.")

    class Meta:
        # Prevent duplicate room type pricing for the same season
        unique_together = ('season', 'room_type')

    def __str__(self):
        return f"{self.room_type} - {self.season.name} ({self.base_price})"



class SalesActivity(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('follow_up', 'Follow-up'),
    ]
    title = models.CharField(max_length=255)
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)
    activity_date = models.DateField()
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    next_follow_up = models.DateField(blank=True, null=True)

    # New sales representative field
    sales_representative = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Link to Django's User model
        on_delete=models.CASCADE,  # Delete sales if the user is deleted
        related_name='sales',  # Optional related name for reverse lookup
    )

    @property
    def is_follow_up_due(self):
        return self.next_follow_up and self.next_follow_up <= date.today()

    def follow_up_due(self):
        """Checks if the next follow-up is overdue (before today)."""
        return self.next_follow_up and self.next_follow_up < now().date()

    def __str__(self):
        return f"{self.title} - {self.operator.name}  by {self.sales_representative.username}"
