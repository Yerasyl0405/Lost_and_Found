from django.db import models
from django.db import models

class LostItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date_lost = models.DateField()
    image = models.ImageField(upload_to='lost_items/', blank=True, null=True)
    is_recovered = models.BooleanField(default=False)  # New field

    def __str__(self):
        return self.name

class FoundItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date_found = models.DateField()
    image = models.ImageField(upload_to='found_items/', blank=True, null=True)
    is_claimed = models.BooleanField(default=False)  # New field

    def __str__(self):
        return self.name
