from django.apps import AppConfig


class BaseAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Base_App'

    def ready(self):
        from .admin_dashboard import register_cms_admin_page
        register_cms_admin_page()
