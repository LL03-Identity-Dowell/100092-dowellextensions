from django.urls import path
from .views import DowellGroupList, DowellGroupDetail

urlpatterns = [
    path('v1/dowellgroups/', DowellGroupList.as_view(), name='dowellgroup'),
    path('v1/dowellgroups/<str:group_id>/',DowellGroupDetail.as_view(), name='dowellgroup_detail'),
]
