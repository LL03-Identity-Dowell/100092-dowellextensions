from django.urls import path
from .views import AnnouncementListCreateView, AnnouncementRetrieveUpdateDestroyView

urlpatterns = [
    path('', AnnouncementListCreateView.as_view()),
    path('<int:pk>/',
         AnnouncementRetrieveUpdateDestroyView.as_view()),
]
