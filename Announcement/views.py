from rest_framework.response import Response
from .serializers import AnnouncementSerializer
from utils.general import logger
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.views import APIView
from utils.dowell_db_call import (
    fetch_document,
    ANNOUNCEMENT_COLLECTION
)
import json


class AnnouncementList(APIView):

    def get(self, request, format=None):

        type_param = request.query_params.get('type')
        user_id = request.query_params.get('user_id')
        org_id = request.query_params.get('org_id')
        member_type = request.query_params.get('member_type')

        type_mapping = {
            'admin': {
                'announcement.deleted': False,
            },
            'my-channel-history': {
                'announcement.deleted': False,
                'announcement.user_id': user_id
            },
            'extension': {
                'announcement.is_active': True,
                'announcement.deleted': False
            }
        }

        if not type_param:
            return Response({"message": "Missing type parameter."}, status=status.HTTP_400_BAD_REQUEST)

        if type_param not in type_mapping:
            return Response({"message": "Invalid type parameter."}, status=status.HTTP_400_BAD_REQUEST)

        if not user_id:
            return Response({"message": "Missing user_id parameter."}, status=status.HTTP_400_BAD_REQUEST)

        fields = type_mapping[type_param]

        if not member_type:
            return Response({"message": "Missing member_type parameter."}, status=status.HTTP_400_BAD_REQUEST)

        if member_type not in ['Public', 'Member', 'User']:
            return Response({"message": "Invalid member_type parameter."}, status=status.HTTP_400_BAD_REQUEST)

        if member_type == 'Member' and not org_id:
            return Response({"message": "Missing org_id parameter for member_type 'Member'."}, status=status.HTTP_400_BAD_REQUEST)

        if member_type == 'User' and not user_id:
            return Response({"message": "Missing user_id parameter for member_type 'User'."}, status=status.HTTP_400_BAD_REQUEST)

        if member_type == 'Public':
            fields['announcement.member_type'] = member_type

        if member_type == 'Member':
            fields["announcement.org_id"] = org_id

        if member_type == 'User':
            fields["announcement.user_id"] = user_id

        if type_param == "my-channel-history":
            fields = type_mapping[type_param]

        try:
            response_json = fetch_document(
                collection=ANNOUNCEMENT_COLLECTION,
                fields=fields
            )


            # serializer = AnnouncementSerializer(response_json)
            for response in response_json['data']:
                announcement = response['announcement']
                if "link" in announcement:
                    pass
                else:
                    announcement['link'] = None
                if "image_url" in announcement:
                    pass
                else:
                    announcement['link'] = None

                if "user_id" in response['announcement'] and response['announcement']['user_id'] == user_id:
                    response['announcement']['option_to_delete'] = True
                    response['announcement']['option_to_edit'] = True
                else:
                    response['announcement']['option_to_delete'] = False
                    response['announcement']['option_to_edit'] = False
                if "link" in response["announcement"]:
                    pass
                else:
                    response['announcement']['link'] = None
            return Response(response_json)

        except Exception as e:
            logger.error(f"Bad Request, {str(e)}")
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            data = request.data
            serializer = AnnouncementSerializer(data=data)
            if serializer.is_valid():
                response = serializer.save()
                return Response(response, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            logger.error(str(e))
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AnnouncementDetail(APIView):
    def get(self, request, id, format=None):
        try:
            response_json = fetch_document(
                collection=ANNOUNCEMENT_COLLECTION,
                fields={
                    "_id": id
                },
            )
            if response_json["isSuccess"] and response_json['data']:
                announcement = response_json["data"][0]['announcement']
                if "link" in announcement:
                    pass
                else:
                    announcement['link'] = None
                if "image_url" in announcement:
                    pass
                else:
                    announcement['link'] = None


            return Response(response_json)

        except Exception as e:
            logger.error(f"Announcement not found, {str(e)}")
            Response(
                {"message": f"Announcement not found, {str(e)}"},
                status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id, format=None):
        try:
            response = fetch_document(
                collection=ANNOUNCEMENT_COLLECTION,
                fields={
                    "_id": id
                },
            )

            if response["isSuccess"] and response['data']:
                announcement = response["data"][0]['announcement']
                announcement['is_active'] = not announcement['is_active']
                response = AnnouncementSerializer.patch(
                    id, announcement)

            else:
                logger.error(f"Announcement Not Found For {id}")
                return Response(
                    {"message": f"Announcement Not Found For {id}"},
                    status=status.HTTP_404_NOT_FOUND)

            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            logger.error(str(e))
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, id, format=None):
        try:
            body = json.loads(request.body)
            response = fetch_document(
                collection=ANNOUNCEMENT_COLLECTION,
                fields={
                    "_id": id
                },
            )

            if response["isSuccess"] and response['data']:
                announcement = response["data"][0]['announcement']
                announcement['description'] = body.get(
                    'description', announcement['description'])
                announcement['product'] = body.get(
                    'product', announcement['product'])
                
                announcement['member_type'] = body.get(
                    'member_type', announcement['member_type'])
                announcement['title'] = body.get(
                    'title', announcement['title'])

                if "image_url" in announcement:
                    announcement['image_url'] = body.get(
                        'image_url', announcement['image_url'])
                else:
                    announcement['image_url'] = body.get('image_url', None)

                if "product_id" in announcement:
                    announcement['product_id'] = body.get(
                        'product_id', announcement['product_id'])
                else:
                    announcement['product_id'] = body.get('product_id', None)

                if "link" in announcement:
                    announcement['link'] = body.get('link',announcement['link'])
                else:
                    announcement['link'] = body.get('link',None)

                response = AnnouncementSerializer.patch(
                    id, announcement)

            else:
                logger.error(f"Announcement Not Found For {id}")
                return Response(
                    {"message": f"Announcement Not Found For {id}"},
                    status=status.HTTP_404_NOT_FOUND)

            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            logger.error(str(e))
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, id, format=None):
        try:
            response = fetch_document(
                collection=ANNOUNCEMENT_COLLECTION,
                fields={
                    "_id": id
                },
            )

            if response["isSuccess"] and response['data']:
                announcement = response["data"][0]['announcement']
                announcement['deleted'] = True
                response = AnnouncementSerializer.patch(
                    id, announcement)

            else:
                logger.error(f"Announcement Not Found For {id}")
                return Response(
                    {"message": f"Announcement Not Found For {id}"},
                    status=status.HTTP_404_NOT_FOUND)

            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            logger.error(str(e))
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(('DELETE',))
def delete_all(request):
    member_type = request.query_params.get('member_type')
    if member_type not in ['Public','Member','User']:
        print(member_type)
        return Response({"message": "Invalid member_type parameter."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        responses = fetch_document(
            collection=ANNOUNCEMENT_COLLECTION,
            fields={
                'announcement.member_type':member_type
            }
        )
    
        for response in responses['data']:
            id = response["_id"]
            announcement = response['announcement']
            announcement['deleted'] = True
            response = AnnouncementSerializer.patch(
                id,
                announcement)
        return Response(responses, status=status.HTTP_200_OK)
        
    except Exception as e:
        logger.error(f"Bad Request, {str(e)}")
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
