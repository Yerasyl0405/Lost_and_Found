# items/serializers.py
from datetime import timezone

from rest_framework import serializers
from .models import FoundItem, LostItem
# items/serializers.py

from rest_framework import serializers
from .models import LostItem
class LostItemSerializer(serializers.ModelSerializer):
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = LostItem
        fields = '__all__'

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Item name must be at least 3 characters long.")
        return value

    def validate_description(self, value):
        if not value:
            raise serializers.ValidationError("Description cannot be empty.")
        return value

    def validate(self, attrs):
        if 'location' in attrs and not attrs['location']:
            raise serializers.ValidationError({"location": "Location is required."})
        return attrs






class FoundItemSerializer(serializers.ModelSerializer):
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = FoundItem
        fields = '__all__'

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Item name must be at least 3 characters.")
        return value

    def validate_description(self, value):
        if not value.strip():
            raise serializers.ValidationError("Description is required.")
        return value

    def validate(self, data):
        if data.get("date_found") and data["date_found"] > timezone.now().date():
            raise serializers.ValidationError({"date_found": "Date cannot be in the future."})
        return data
