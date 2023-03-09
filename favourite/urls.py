from django.urls import path
from .views import *

urlpatterns = [
    path('favourite/',setasfavourite.as_view()),
    path('favourite/<int:pk>',setasfavourite.as_view()),

]