import os

from django.core.files.storage import get_storage_class
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timezone import now
from enum import Enum

from items.storages import MediaStorage

User = get_user_model()


class LostItemStatus(Enum):
    LOST = "lost"
    FOUND = "found"
    RECOVERED = "recovered"


class FoundItemStatus(Enum):
    FOUND = "found"
    CLAIMED = "claimed"


def get_media_storage():
    if os.environ.get("DISABLE_MINIO") == "1":
        return None  # Использует стандартное хранилище Django
    from items.storages import MediaStorage
    return get_storage_class("items.storages.MediaStorage")()



class LostItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date_lost = models.DateField()

    image = models.ImageField(
        upload_to="lost_items/",
        storage=get_media_storage(),  # None, если отключено
        blank=True,
        null=True
    )
    is_recovered = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=now)
    status = models.CharField(
        max_length=10,
        choices=[(status.value, status.name.title()) for status in LostItemStatus],
        default=LostItemStatus.LOST.value
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.get_status_display()}"

    @property
    def is_lost(self):
        return self.status == LostItemStatus.LOST.value

    @property
    def is_found(self):
        return self.status == LostItemStatus.FOUND.value





class FoundItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date_found = models.DateField()

    image = models.ImageField(
        upload_to="found_items/",
        storage=get_media_storage(),  # None, если отключено
        blank=True,
        null=True
    )
    is_claimed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=now)
    status = models.CharField(
        max_length=10,
        choices=[(status.value, status.name.title()) for status in FoundItemStatus],
        default=FoundItemStatus.FOUND.value
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.get_status_display()}"

    @property
    def is_found_unclaimed(self):
        return self.status == FoundItemStatus.FOUND.value and not self.is_claimed



   