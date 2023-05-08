from rest_framework import serializers
from .models import Announcement


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ('id', 'message', 'created_at',
                  'product', 'created_by', 'is_active')
        read_only_fields = ('id', 'created_at')
