from django.apps import AppConfig


class ItemsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'items'


def ready(self):
    from .startup import ensure_media_bucket
    ensure_media_bucket()
