from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class LostItem(models.Model):
    name = models.CharField(max_length=200)

    description = models.TextField()
    location = models.CharField(max_length=255)
    date_lost = models.CharField(max_length=255)
    image = models.ImageField(upload_to="lost_items/", blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

class FoundItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date_found = models.CharField(max_length=255)
    image = models.ImageField(upload_to="found_items/", blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.name


