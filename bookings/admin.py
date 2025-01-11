from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('operator', 'check_in', 'check_out', 'number_of_guests', 'total_price')
    search_fields = ('operator__name', 'check_in', 'check_out')
    list_filter = ('check_in', 'check_out')