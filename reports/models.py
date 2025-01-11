from django.db import models

class Report(models.Model):
    REPORT_TYPES = [
        ('booking_summary', 'Booking Summary'),
        ('sales_summary', 'Sales Summary'),
    ]

    name = models.CharField(max_length=255)
    report_type = models.CharField(max_length=20, choices=REPORT_TYPES)
    generated_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.get_report_type_display()})"