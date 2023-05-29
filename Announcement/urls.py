from django.urls import path
from .views import AnnouncementListCreateView, AnnouncementRetrieveUpdateDestroyView

urlpatterns = [
    path('announcements/', AnnouncementListCreateView.as_view()),
    path('announcements/<int:pk>/',
         AnnouncementRetrieveUpdateDestroyView.as_view()),
]
