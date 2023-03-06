from django.urls import path
from notifications.views import *

urlpatterns = [
    path('serverStatus/',serverStatus.as_view()),
    path('testdatabase/',testdatabase.as_view()),
]