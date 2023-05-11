from rest_framework import serializers
from .models import Announcement


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ('id', 'description', 'created_at',
                  'product', 'created_by', 'is_active', 'member_type', 'company_id', 'created_at_position')
        read_only_fields = ('id', 'created_at')
