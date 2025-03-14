from django.contrib import admin
from .models import LostItem, FoundItem
from django.contrib import admin
from .models import LostItem, FoundItem

@admin.register(LostItem)
class LostItemAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "location", "date_lost", "status", "is_recovered")  # ✅ Ensure status exists
    list_filter = ("status", "is_recovered")  # ✅ Ensure status exists
    search_fields = ("name", "location", "description")


@admin.register(FoundItem)
class FoundItemAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "location", "date_found", "status", "is_claimed")  # ✅ Ensure status exists
    list_filter = ("status", "is_claimed")  # ✅ Ensure status exists
    search_fields = ("name", "location", "description")
