from django.urls import path
from notifications.views import *

urlpatterns = [
    path('v1/notifications/products/', ProductNotificationList.as_view()),
    path('v1/notifications/products/<str:document_id>/', ProductNotificationDetail.as_view()),

    path('v1/notifications/', NotificationList.as_view(), name='notification_list'),
    path('v1/notifications/<str:document_id>/', NotificationDetail.as_view(),
         name='notification_detail'),

]
