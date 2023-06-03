from django.urls import path
from notifications.views import *

urlpatterns = [
    path('products/', ProductNotificationList.as_view()),
    path('products/<str:document_id>/', ProductNotificationDetail.as_view()),

    path('', NotificationList.as_view(), name='notification_list'),
    path('<str:document_id>/', NotificationDetail.as_view(),
         name='notification_detail'),

]
