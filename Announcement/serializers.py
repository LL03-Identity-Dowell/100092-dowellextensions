from rest_framework import serializers
from .models import Announcement
from utils.general import logger
from datetime import datetime
from utils.dowell_db_call import (
    save_document,
    update_document,
    ANNOUNCEMENT_COLLECTION
)


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'

    def create(self, validated_data):
        try:
            validated_data['created_at'] = datetime.utcnow().isoformat()
            validated_data['is_Active'] = True
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
