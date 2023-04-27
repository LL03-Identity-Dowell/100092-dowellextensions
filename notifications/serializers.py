from rest_framework import serializers
from .models import *


class sendProductNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noftification
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
