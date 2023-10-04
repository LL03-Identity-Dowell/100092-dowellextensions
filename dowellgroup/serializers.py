from rest_framework import serializers
from utils.general import logger
from datetime import datetime
from utils.dowell_db_call import (
    save_document,
    update_document,
    DOWELL_GROUP_COLLECTION
)


class DowellGroupSerializer(serializers.Serializer):
    group_name = serializers.CharField(max_length=255, required=True)
    user_id = serializers.CharField(max_length=255, required=True)
    created_by = serializers.CharField(max_length=255, required=True)
    org_id = serializers.CharField(max_length=255, required=True)
    org_name = serializers.CharField(max_length=255, required=True)
    created_at_position = serializers.CharField(max_length=255, required=True)
    load_from_csv = serializers.BooleanField(default=False)
    group_detail = serializers.ListField(required=True)

    def create(self, validated_data):
        try:
            validated_data['created_at'] = datetime.utcnow().isoformat()
            validated_data['deleted'] = False
            validated_data['share_usernames'] = []
            # Remove later
            validated_data['email_list'] = []

            response = save_document(
                collection=DOWELL_GROUP_COLLECTION,
                value=validated_data,
            )
            return response

        except Exception as e:
            logger.info(f"Group Not Saved: ({e})")
            raise ValueError(f"Group Not Saved: ({e})")

    @staticmethod
    def update(document_id, document):
        try:
            response = update_document(
                collection=DOWELL_GROUP_COLLECTION,
                new_value=document,
                document_id=document_id
            )
            return response

        except Exception as e:
            logger.info(f"Group Not Saved: ({e})")
            raise ValueError(f"Group Not Saved: ({e})")
