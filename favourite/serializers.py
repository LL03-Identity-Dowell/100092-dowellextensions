from rest_framework import serializers
from .models import *


class favouriteSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=300)
    portfolio = serializers.CharField(max_length=300)
    productName = serializers.CharField(max_length=300)
    action = serializers.BooleanField(default= True)
    orgName = serializers.CharField(max_length=300)
    image = serializers.ImageField(required=False)
    image_url = serializers.URLField(required=False)


class ImageSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    session_id = serializers.CharField(max_length=300)
    username = serializers.CharField(max_length=300)
    image = serializers.CharField()

    # image = serializers.ReadOnlyField()
    # class Meta:
    #     model = FavouriteImage
    #     fields = ('id', 'session_id', 'username', 'image')

        