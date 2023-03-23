from rest_framework import serializers
from .models import *


class favouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = favourite
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):

    # image = serializers.ReadOnlyField()
    class Meta:
        model = FavouriteImage
        fields = ('id', 'session_id', 'username', 'image')

        