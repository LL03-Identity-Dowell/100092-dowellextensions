from django.urls import path
from .views import AnnouncementList, AnnouncementDetail

urlpatterns = [
    path('v1/announcements/', AnnouncementList.as_view(), name='announcement'),
    path('v1/announcements/<str:id>/',
         AnnouncementDetail.as_view(), name='announcement_detail'),
]
