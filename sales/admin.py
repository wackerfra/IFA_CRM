from django.contrib import admin
from .models import SalesActivity

@admin.register(SalesActivity)
class SalesActivityAdmin(admin.ModelAdmin):
    list_display = ('activity_date', 'status', 'next_follow_up', 'follow_up_due')
    search_fields = ('description', 'status')
    list_filter = ('status', 'activity_date')