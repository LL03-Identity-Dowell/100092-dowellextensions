from django.urls import path
from .views import *

urlpatterns = [
    path('postfavourite/',postfavourite.as_view()),
    path('putfavourite/<int:pk>',postfavourite.as_view()),

]