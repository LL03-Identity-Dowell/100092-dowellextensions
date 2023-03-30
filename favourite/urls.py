from django.urls import path, include
from .views import *

urlpatterns = [
    path('favourite/',setasfavourite.as_view()),
    path('favourite/<int:pk>',setasfavourite.as_view()),
    path('favouriteIcon/',favouriteIcon.as_view()),
    path('favouriteImage/', FavouriteImageView.as_view()),
    path('favouriteImage/<str:username>', FavouriteImageView.as_view())
]