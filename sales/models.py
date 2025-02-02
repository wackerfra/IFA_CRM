from django.contrib.auth.models import User
from django.db import models
from datetime import date
from operators.models import Operator
from django.utils.timezone import now
from django.conf import settings




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
