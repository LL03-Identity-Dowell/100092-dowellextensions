from rest_framework import serializers
from utils.general import logger
from datetime import datetime
from utils.dowell_db_call import (
    save_document,
    update_document,
    ANNOUNCEMENT_COLLECTION
)


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
    image_url = serializers.URLField(required = False, allow_blank=True)
    link = serializers.CharField(max_length=500,required = False, allow_blank=True)

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



class AnnouncementListSerializer(serializers.Serializer):
    type = serializers.ChoiceField(
        choices=['admin', 'my-channel-history', 'extension'])
    user_id = serializers.CharField()
    org_id = serializers.CharField(required=False)
    member_type = serializers.ChoiceField(choices=['Public', 'Member', 'User'])

    def validate(self, data):
        type_mapping = {
            'admin': {
                'announcement.deleted': False,
            },
            'my-channel-history': {
                'announcement.deleted': False,
                'announcement.user_id': data['user_id']
            },
            'extension': {
                'announcement.is_active': True,
                'announcement.deleted': False
            }
        }

        if data['type'] not in type_mapping:
            raise serializers.ValidationError(
                {"message": "Invalid type parameter."})

        if data['member_type'] == 'Member' and not data.get('org_id'):
            raise serializers.ValidationError(
                {"message": "Missing org_id parameter for member_type 'Member'."})

        if data['member_type'] == 'User' and not data.get('user_id'):
            raise serializers.ValidationError(
                {"message": "Missing user_id parameter for member_type 'User'."})

        if data['member_type'] == 'Public':
            type_mapping[data['type']]['announcement.member_type'] = 'Public'
        elif data['member_type'] == 'Member':
            type_mapping[data['type']]['announcement.member_type'] = 'Member'
        elif data['member_type'] == 'User':
            type_mapping[data['type']]['announcement.member_type'] = 'User'

        if data['member_type'] == 'Member':
            type_mapping[data['type']]['announcement.org_id'] = data['org_id']

        if data['member_type'] == 'User':
            type_mapping[data['type']
                         ]['announcement.user_id'] = data['user_id']

        data['fields'] = type_mapping[data['type']]
        return data
    

class AnnouncementRestoreSerializer(serializers.Serializer):
    org_id = serializers.CharField(required=False)
    member_type = serializers.ChoiceField(choices=['Public', 'Member', 'User'])
    def validate(self,data):
        fields = {}
        if not data["org_id"]:
            raise serializers.ValidationError(
                {"message":"Missing parameter 'org_id' "}
                )
        fields["announcement.org_id"]=data["org_id"]

        if data["member_type"] not in ['Public','Member','User']:
            raise serializers.ValidationError(
                {"message":"Invalid parameter 'member_type' "}
            )
        fields["announcement.member_type"]=data["member_type"]

        data["fields"] = fields  
        return data
