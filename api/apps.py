from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

class APP_NAMEConfig(AppConfig):
    name = 'APP_NAME'
    icon = 'ICON_CLASS'  # for example: icon = 'fa fa-users'
