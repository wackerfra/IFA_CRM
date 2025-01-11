from django.contrib import admin
from .models import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('name', 'report_type', 'generated_at')
    search_fields = ('name', 'report_type')
    list_filter = ('report_type', 'generated_at')