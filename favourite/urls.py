from django.urls import path, include
from .views import *

urlpatterns = [
    path('favourite/',setasfavourite.as_view()),
    path('favourite/<int:pk>',setasfavourite.as_view()),
    path('favourites/<str:user_id>',FavouritesView.as_view()),
    path('favouriteIcon/',favouriteIcon.as_view()),
    path('v1/favorites/<str:user_id>/images/', FavouriteImageList.as_view()),
    path('v1/favorites/<str:user_id>/images/<str:favorite_img_id>/', FavouriteImageDetail.as_view())
]