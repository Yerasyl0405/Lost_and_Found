from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timezone import now

User = get_user_model()

class LostItem(models.Model):
    STATUS_CHOICES = [
        ("lost", "Lost"),
        ("found", "Found"),
        ("recovered", "Recovered"),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date_lost = models.DateField()
    image = models.ImageField(upload_to="lost_items/", blank=True, null=True)
    is_recovered = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="lost")  # ✅ Add status field

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.get_status_display()}"


class FoundItem(models.Model):
    STATUS_CHOICES = [
        ("found", "Found"),
        ("claimed", "Claimed"),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date_found = models.DateField()
    image = models.ImageField(upload_to="found_items/", blank=True, null=True)
    is_claimed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="found")  # ✅ Add status field

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.get_status_display()}"
