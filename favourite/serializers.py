from rest_framework import serializers
from .models import *


class favouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = favourite
        fields = '__all__'
        