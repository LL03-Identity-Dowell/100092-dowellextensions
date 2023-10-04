from rest_framework import serializers
from .models import *
from utils.general import logger
from datetime import datetime
from utils.dowell_db_call import (
    save_document,
    update_document,
    FAVORITE_COLLECTION
)
 
 
class favouriteSerializer(serializers.Serializer):
    user_id = serializers.CharField(max_length=50)
    username = serializers.CharField(max_length=300)
    portfolio = serializers.CharField(max_length=300)
    product_name = serializers.CharField(max_length=300)
    product_id = serializers.CharField(max_length=300)
    org_id = serializers.CharField(max_length=255, required=True)
    org_name = serializers.CharField(max_length=255, required=True)
    image_url = serializers.URLField(required=False)

    def create(self, validated_data):
        try:
            validated_data['type'] = "favorite"
            validated_data['deleted'] = False
            validated_data['created_at'] = datetime.utcnow().isoformat()
            response = save_document(
                collection=FAVORITE_COLLECTION,
                value=validated_data
            )
            return response
        except Exception as e:
            logger.info(f"Favorite Not Saved: ({e})")
            raise ValueError(f"Favorite Not Saved: ({e})")

    @staticmethod
    def update(document_id, document):
        try:
            response = update_document(
                collection=FAVORITE_COLLECTION,
                new_value=document,
                document_id=document_id
            )
            return response

        except Exception as e:
            logger.info(f"Favorite Not Updated: ({e})")
            raise ValueError(f"Favorite Not Updated: ({e})")
        

class ImageSerializer(serializers.Serializer):
    session_id = serializers.CharField(max_length=300)
    user_id = serializers.CharField(max_length=50)
    username = serializers.CharField(max_length=300)
    image_url = serializers.URLField()

    def create(self, validated_data):
        try:
            validated_data['created_at'] = datetime.utcnow().isoformat()
            validated_data['deleted'] = False
            validated_data['type'] = "favorite-image"

            response = save_document(
                collection=FAVORITE_COLLECTION,
                value=validated_data,
            )
            return response

        except Exception as e:
            logger.info(f"Favorite Image Not Saved: ({e})")
            raise ValueError(f"Favorite Image Not Saved: ({e})")

    @staticmethod
    def update(document_id, document):
        try:
            response = update_document(
                collection=FAVORITE_COLLECTION,
                new_value=document,
                document_id=document_id
            )
            return response

        except Exception as e:
            logger.info(f"Favorite Image Not Saved: ({e})")
            raise ValueError(f"Favorite Image Not Saved: ({e})")
