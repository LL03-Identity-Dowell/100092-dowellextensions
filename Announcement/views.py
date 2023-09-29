from rest_framework.response import Response
from .serializers import AnnouncementSerializer, AnnouncementListSerializer, AnnouncementRestoreSerializer
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
        serializer = AnnouncementListSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        try:
            fields = serializer.validated_data['fields']
            response_json = fetch_document(
                collection=ANNOUNCEMENT_COLLECTION,
                fields=fields
            )
 
            user_id = serializer.validated_data['user_id']
            for response in response_json['data']:
                if "user_id" in response['announcement'] and response['announcement']['user_id'] == user_id:
                    response['announcement']['option_to_delete'] = True
                    response['announcement']['option_to_edit'] = True
                else:
                    response['announcement']['option_to_delete'] = False
                    response['announcement']['option_to_edit'] = False

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
                #serializer should take announcement
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

@api_view(("PUT",))        
def restore_announcements(request):
    serializer = AnnouncementRestoreSerializer(data=request.query_params)
    serializer.is_valid(raise_exception=True)
    try:
        fields = serializer.validated_data["fields"]
        responses = fetch_document(
            collection=ANNOUNCEMENT_COLLECTION,
            fields=fields
        )
        for response in responses['data']:
            id = response["_id"]
            announcement = response['announcement']
            announcement['deleted'] = False
            response = AnnouncementSerializer.patch(
                id,
                announcement)
        return Response(responses, status=status.HTTP_200_OK)
    except Exception as e:
        logger.error(f"Bad Request, {str(e)}")
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)



