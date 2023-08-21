from django.urls import include, path
from .views import health


app_name = "healthcheck"
urlpatterns = [
    path('', health, name='health'),
    path('health/', health, name='health_1'),
]