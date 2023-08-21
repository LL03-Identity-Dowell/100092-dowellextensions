from django.urls import path
from .views import AnnouncementList, AnnouncementDetail,delete_all

urlpatterns = [

    path('v1/announcements/', AnnouncementList.as_view(), name='announcement'),
    path('v1/announcements/delete_all/',delete_all,name="delete"),
    path('v1/announcements/<str:id>/',
         AnnouncementDetail.as_view(), name='announcement_detail'),

]
