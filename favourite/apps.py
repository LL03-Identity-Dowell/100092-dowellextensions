from django.apps import AppConfig


class FavouriteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'favourite'

class FavouriteImageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'FavouriteImage'
