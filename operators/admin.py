from django.contrib import admin
from .models import Hotel, Operator, OperatorInterest

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'capacity']


@admin.register(Operator)
class OperatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_person', 'phone', 'email', 'city', 'country', 'internet', 'segment')
    search_fields = ('name', 'contact_person', 'email', 'city', 'segment')
    list_filter = ('country','segment')


@admin.register(OperatorInterest)
class OperatorInterestAdmin(admin.ModelAdmin):
    list_display = ['operator', 'hotel', 'priority', 'agreement_date']
    list_filter = ['priority', 'agreement_date', 'hotel']  # Add filters for better usability