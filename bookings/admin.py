from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('operator', 'hotel', 'segment', 'double_rooms', 'single_rooms','check_in', 'check_out',
                    'number_of_guests', 'total_price','sales_representative')
    search_fields = ('operator__name', 'hotel','check_in', 'check_out','sales_representative__username')
    list_filter = ('check_in', 'check_out', 'hotel','sales_representative')