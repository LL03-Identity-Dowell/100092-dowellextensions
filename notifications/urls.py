from django.urls import path
from notifications.views import *

urlpatterns = [
    path('serverStatus/',serverStatus.as_view()),
    path('notification/',notification.as_view()),
    path('notification/<str:document_id>',notification.as_view()),

]