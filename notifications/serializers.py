from rest_framework import serializers
from .models import *


class sendProductNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noftification
        fields = '__all__'