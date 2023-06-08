from rest_framework import serializers
from .models import Announcement
from utils.general import logger
from datetime import datetime
from utils.dowell_db_call import (
    save_document,
    update_document,
    ANNOUNCEMENT_COLLECTION
)


# class AnnouncementSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Announcement
#         fields = ('id', 'description', 'created_at',
#                   'product', 'created_by', 'is_active', 'member_type', 'company_id', 'created_at_position')
#         read_only_fields = ('id', 'created_at')


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'

    def create(self, validated_data):
        try:
            # Include additional attribute
            validated_data['created_at'] = datetime.utcnow().isoformat()
            validated_data['is_Active'] = True
            # Save data
            response = save_document(
                collection=ANNOUNCEMENT_COLLECTION,
                value=validated_data,
            )
            return response

        except Exception as e:
            logger.info(f"Announcement Not Saved: ({e})")
            raise ValueError(f"Announcement Not Saved: ({e})")

    def update(self, document: dict, validated_data):
        try:
            # Save data
            response = update_document(
                collection=ANNOUNCEMENT_COLLECTION,
                is_Active=True
                # new_value=validated_data,
                # document_id=document['document_id']
            )
            return response

        except Exception as e:
            logger.info(f"Announcement Not Saved: ({e})")
            raise ValueError(f"Announcement Not Saved: ({e})")

    @staticmethod
    def patch(document_id, document):
        try:
            # Save data
            response = update_document(
                collection=ANNOUNCEMENT_COLLECTION,
                new_value=document,
                document_id=document_id
            )
            return response

        except Exception as e:
            logger.info(f"Announcement Not Saved: ({e})")
            raise ValueError(f"Announcement Not Saved: ({e})")
