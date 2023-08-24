from rest_framework import serializers
from .models import *
from utils.general import logger
from datetime import datetime
from utils.dowell_db_call import (
    save_document,
    update_document,
    NOTIFICATION_COLLECTION
    )

class ProductNotificationSerializer(serializers.Serializer):
    created_by = serializers.CharField(max_length=300)
    org_name = serializers.CharField(max_length=300)
    org_id = serializers.CharField(max_length=255)
    product = serializers.CharField(max_length=300)
    portfolio = serializers.CharField(max_length=300)
    product_name = serializers.CharField(max_length=300)
    title = serializers.CharField(max_length=500)
    message = serializers.CharField(max_length=500)

    #required can be set to false
    link = serializers.CharField(max_length=2048)
    duration = serializers.CharField(max_length=300)
    button_status = serializers.CharField(max_length=300)


    def create(self, validated_data):
        try:
            # Include additional attribute
            validated_data['created_at'] = datetime.utcnow().isoformat()
            validated_data['seen'] = False
            validated_data['seen_at'] = None
            validated_data['document_type'] = "product_notification"
            validated_data['deleted'] = False

            # Save data
            response = save_document(
                collection=NOTIFICATION_COLLECTION,
                value=validated_data,
            )
            return response
        
        except Exception as e:
            logger.info(f"Notification Not Saved: ({e})")
            raise ValueError(f"Notification Not Saved: ({e})")
    

    def update(self, document:dict, validated_data):
        try:
            # Save data
            response = update_document(
                collection=NOTIFICATION_COLLECTION,
                new_value=validated_data,
                document_id=document['document_id']
            )
            return response
        
        except Exception as e:
            logger.info(f"Notification Not Saved: ({e})")
            raise ValueError(f"Notification Not Saved: ({e})")
        
    @staticmethod
    def patch(document_id, document):
        try:
            # Save data
            response = update_document(
                collection=NOTIFICATION_COLLECTION,
                new_value=document,
                document_id=document_id
            )
            return response
        
        except Exception as e:
            logger.info(f"Notification Not Saved: ({e})")
            raise ValueError(f"Notification Not Saved: ({e})")

    


class NotificationSerializer(serializers.Serializer):
    data_type = serializers.CharField(max_length=255)
    user_type = serializers.CharField(max_length=255)
    from_field = serializers.CharField(max_length=255)
    to = serializers.CharField(max_length=255)
    desc = serializers.CharField()
    meant_for = serializers.CharField(max_length=255)
    type_of_notification = serializers.CharField(max_length=255)
    created_by = serializers.CharField(max_length=300)
    org_name = serializers.CharField(max_length=300)
    org_id = serializers.CharField(max_length=255)



    def create(self, validated_data):
        try:
            # Include additional attribute
            validated_data['created_at'] = datetime.utcnow().isoformat()
            validated_data['seen'] = False
            validated_data['seen_at'] = None
            validated_data['document_type'] = "notification"
            validated_data['deleted'] = False

            # Save data
            response = save_document(
                collection=NOTIFICATION_COLLECTION,
                value=validated_data,
            )
            return response
        
        except Exception as e:
            logger.info(f"Notification Not Saved: ({e})")
            raise ValueError(f"Notification Not Saved: ({e})")
    

    def update(self, document:dict, validated_data):
        try:
            # Save data
            response = update_document(
                collection=NOTIFICATION_COLLECTION,
                new_value=validated_data,
                document_id=document['document_id']
            )
            return response
        
        except Exception as e:
            logger.info(f"Notification Not Saved: ({e})")
            raise ValueError(f"Notification Not Saved: ({e})")
        
    @staticmethod
    def patch(document_id, document):
        try:
            # Save data
            response = update_document(
                collection=NOTIFICATION_COLLECTION,
                new_value=document,
                document_id=document_id
            )
            return response
        
        except Exception as e:
            logger.info(f"Notification Not Saved: ({e})")
            raise ValueError(f"Notification Not Saved: ({e})")

    