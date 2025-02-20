from django.contrib import admin
from .models import SalesActivity,HotelSeason, HotelSeasonPricing


@admin.register(SalesActivity)
class SalesActivityAdmin(admin.ModelAdmin):
    list_display = ('activity_date', 'status', 'next_follow_up', 'follow_up_due','sales_representative')
    search_fields = ('description', 'status','sales_representative')
    list_filter = ('status', 'activity_date','sales_representative__username')



@admin.register(HotelSeason)
class HotelSeasonAdmin(admin.ModelAdmin):
    list_display = ('name', 'hotel', 'start_date', 'end_date')
    list_filter = ('hotel',)
    search_fields = ('name', 'hotel__name')  # Search by season name or hotel name


@admin.register(HotelSeasonPricing)
class HotelSeasonPricingAdmin(admin.ModelAdmin):
    list_display = ('room_type', 'season', 'base_price', 'weekend_price')
    list_filter = ('season__hotel', 'season__name')
    search_fields = ('room_type', 'season__name', 'season__hotel__name')
