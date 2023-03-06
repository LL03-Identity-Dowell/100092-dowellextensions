from django.urls import path
from notifications.views import *

urlpatterns = [
    path('serverStatus/',serverStatus.as_view()),
    path('sendProductNotification/',sendProductNotification.as_view()),
    path('putProductNotification/<int:pk>',sendProductNotification.as_view()),

]