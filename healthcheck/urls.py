from django.urls import include, path
from .views import health, delete_all


app_name = "healthcheck"
urlpatterns = [
    path('', health, name='health'),
    path('health/', health, name='health_1'),
    path('delete/',delete_all,name="delete")
]