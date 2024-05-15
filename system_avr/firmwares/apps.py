from django.apps import AppConfig


class FirmwaresConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'firmwares'

    def ready(self) -> None:
        import firmwares.signals
