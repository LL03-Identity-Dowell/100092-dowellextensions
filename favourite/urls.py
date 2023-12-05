from django.urls import path, include
from .views import *

urlpatterns = [
    # Old Endpoint
    path('favourite/', Oldsetasfavourite.as_view()),
    path('favourite/<int:pk>', Oldsetasfavourite.as_view()),
    # path('favourites/<str:username>',OldFavouritesView.as_view()),
    path('favouriteIcon/', OldfavouriteIcon.as_view()),
    path('favouriteImage/', OldFavouriteImageView.as_view()),
    path('favouriteImage/<str:username>', OldFavouriteImageView.as_view()),

    # New Endpoint
    path('v1/favorites/', FavouritesView.as_view()),
    path('v1/favorites/<str:pk>/', setasfavourite.as_view()),
    path('v1/users/<str:user_id>/favorites/',
         FavouritesByUserIdView.as_view()),
    path('v1/favorites/<str:user_id>/images/', FavouriteImageList.as_view()),
    path('v1/favorites/<str:user_id>/images/<str:favorite_img_id>/',
         FavouriteImageDetail.as_view())
]
