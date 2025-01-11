from django.contrib import admin
from .models import Operator

@admin.register(Operator)
class OperatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_person', 'phone', 'email', 'city', 'country')
    search_fields = ('name', 'contact_person', 'email', 'city')
    list_filter = ('country',)