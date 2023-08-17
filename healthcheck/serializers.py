from rest_framework import serializers
from utils.dowell_db_call import (
    save_document,
    update_document,
    ANNOUNCEMENT_COLLECTION
)
from utils.general import logger
from Announcement.models import Announcement


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'

    @staticmethod
    def patch(id,document):
        try:
            response = update_document(
                collection=ANNOUNCEMENT_COLLECTION,
                new_value=document,
                document_id=id
            )
            return response

        except Exception as e:
            logger.info(f"Announcement Not Saved: ({e})")
            raise ValueError(f"Announcement Not Saved: ({e})")
