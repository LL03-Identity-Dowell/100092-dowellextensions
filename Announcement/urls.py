from django.urls import path
from .views import AnnouncementList, AnnouncementDetail

urlpatterns = [
    path('v1/announcements/', AnnouncementList.as_view()),
    path('v1/announcements/<str:id>/',
         AnnouncementDetail.as_view()),
]
