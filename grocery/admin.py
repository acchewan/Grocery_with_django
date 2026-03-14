from django.contrib import admin
from .models import GroceryItem


@admin.register(GroceryItem)
class GroceryItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'completed', 'due_date', 'created_at')
    list_filter = ('completed',)
    search_fields = ('name',)
