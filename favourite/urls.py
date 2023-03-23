from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'favouriteImage', FavouriteImageView)

urlpatterns = [
    path('', include(router.urls)),
    path('favourite/',setasfavourite.as_view()),
    path('favourite/<int:pk>',setasfavourite.as_view()),
    path('favouriteIcon/',favouriteIcon.as_view())
]