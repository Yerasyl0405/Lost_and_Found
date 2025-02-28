from django import forms
from .models import LostItem, FoundItem

class LostItemForm(forms.ModelForm):
    class Meta:
        model = LostItem
        fields = ["name", "description", "location", "date_lost", "image"]

class FoundItemForm(forms.ModelForm):
    class Meta:
        model = FoundItem
        fields = ["name", "description", "location", "date_found", "image"]
