from django.urls import path
from .views import AnnouncementList, AnnouncementDetail,delete_all,restore_announcements

urlpatterns = [

    path('v1/announcements/', AnnouncementList.as_view(), name='announcement'),
    path('v1/announcements/delete_all/',delete_all,name="delete"),
    path('v1/announcements/restore/',restore_announcements,name="delete"),    
    path('v1/announcements/<str:id>/',
         AnnouncementDetail.as_view(), name='announcement_detail'),

]
