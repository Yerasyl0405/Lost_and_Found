from django import forms
from .models import LostItem, FoundItem

class LostItemForm(forms.ModelForm):

    class Meta:
        model = LostItem
        fields = ["name", "description", "location", "date_lost", "image", ]
        widgets = {
            "date_lost": forms.DateInput(attrs={"type": "date", "class": "form-control"}),  # Calendar Picker
        }

class FoundItemForm(forms.ModelForm):

    class Meta:
        model = FoundItem
        fields = ["name", "description", "location", "date_found", "image"]
        widgets = {
            "date_found": forms.DateInput(attrs={"type": "date", "class": "form-control"}),  # Calendar Picker
        }
