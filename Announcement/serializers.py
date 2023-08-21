from rest_framework import serializers
from .models import Announcement
from utils.general import logger
from datetime import datetime
from utils.dowell_db_call import (
    save_document,
    update_document,
    ANNOUNCEMENT_COLLECTION
)
import datetime


class AnnouncementSerializer(serializers.Serializer):
    MEMBER_TYPE_CHOICES = (
        ('Public', 'Public'),
        ('Member', 'Member'),
        ('User', 'User'),
    )

    member_type = serializers.ChoiceField(MEMBER_TYPE_CHOICES,required = True)
    description = serializers.CharField(max_length=2028,required = True)
    product  = serializers.CharField(max_length=255,required=True)
    product_id = serializers.CharField(max_length=255,required=True)
    created_by = serializers.CharField(max_length=255,required = True)
    org_id = serializers.CharField(max_length=255,required = True)
    user_id = serializers.CharField(max_length=255,required = True)
    title = serializers.CharField(max_length=255,required = True)
    org_name = serializers.CharField(max_length=255,required = True)
    created_at_position = serializers.CharField(max_length=255,required = True)
    image_url = serializers.CharField(max_length=255,required = False)
    link = serializers.CharField(max_length=500,required = False)

    def create(self, validated_data):
        try:
            validated_data['created_at'] = datetime.utcnow().isoformat()
            validated_data['is_active'] = True
            validated_data['deleted'] = False
            response = save_document(
                collection=ANNOUNCEMENT_COLLECTION,
                value=validated_data,
            )
            return response

        except Exception as e:
            logger.info(f"Announcement Not Saved: ({e})")
            raise ValueError(f"Announcement Not Saved: ({e})")

    @staticmethod
    def patch(document_id, document):
        try:
            response = update_document(
                collection=ANNOUNCEMENT_COLLECTION,
                new_value=document,
                document_id=document_id
            )
            return response

        except Exception as e:
            logger.info(f"Announcement Not Saved: ({e})")
            raise ValueError(f"Announcement Not Saved: ({e})")
        

