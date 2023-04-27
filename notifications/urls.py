from django.urls import path
from notifications.views import *

urlpatterns = [
    path('serverStatus/', serverStatus.as_view()),
    path('notification/', notification.as_view()),
    path('notification/<str:document_id>', notification.as_view()),
    path('notifications/', NotificationList.as_view(), name='notification_list'),
    path('notifications/detail/', NotificationDetail.as_view(),
         name='notification_detail'),

]
