from django.apps import AppConfig


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
    def ready(self):
        # Import the signals here to ensure they are registered
        import myapp.signals