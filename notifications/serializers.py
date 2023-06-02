from rest_framework import serializers
from .models import *
from utils.general import logger
from datetime import datetime
from utils.dowell_db_call import (
    save_document,
    update_document,
    NOTIFICATION_COLLECTION
    )

class ProductNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductNotification
        fields = '__all__'

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
            logger.info(f"Data not saved: ({e})")
            raise ValueError(f"Data not saved: ({e})")
    

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

    


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
