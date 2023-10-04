from django.urls import path, include
from .views import *

urlpatterns = [
    path('favourite/',FavouritesView.as_view()),
    path('favourite/<int:pk>',Oldfavourite.as_view()),
    path('favourites/<str:user_id>',Oldfavourite.as_view()),
    # path('favouriteIcon/',favouriteIcon.as_view()),

    #new endpoints
    path('v1/favorites/',FavouritesView.as_view()),
    # path('v1/favorites/favourite_icon/',favouriteIcon.as_view()),
    path('v1/favorites/<str:pk>/', setasfavourite.as_view()),
    path('v1/users/<str:user_id>/favorites/',FavouritesByUserIdView.as_view()),
    path('v1/favorites/<str:user_id>/images/', FavouriteImageList.as_view()),
    path('v1/favorites/<str:user_id>/images/<str:favorite_img_id>/', FavouriteImageDetail.as_view())
]