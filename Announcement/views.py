from rest_framework.response import Response
from .serializers import AnnouncementSerializer
from utils.general import logger
from rest_framework import status
from rest_framework.views import APIView
from utils.dowell_db_call import (
    fetch_document,
    ANNOUNCEMENT_COLLECTION
)
import json


class AnnouncementList(APIView):

    def get(self, request, format=None):

        type_param = request.query_params.get('type')

        if type_param == 'admin':
            fields = {
                "announcement.deleted": False,
            }
        elif type_param == 'extension':
            fields = {
                "announcement.is_active": True,
                "announcement.deleted": False
            }
        else:
            return Response({"message": "Invalid type parameter."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            response_json = fetch_document(
                collection=ANNOUNCEMENT_COLLECTION,
                fields=fields
            )
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
                announcement['description'] = body.get(
                    'description', announcement['description'])
                announcement['product'] = body.get(
                    'product', announcement['product'])
                announcement['member_type'] = body.get(
                    'member_type', announcement['member_type'])
                announcement['created_by'] = body.get(
                    'created_by', announcement['created_by'])
                announcement['org_id'] = body.get(
                    'org_id', announcement['org_id'])
                announcement['created_at_position'] = body.get(
                    'created_at_position', announcement['created_at_position'])
                announcement['title'] = body.get(
                    'title', announcement['title'])
                announcement['org_name'] = body.get(
                    'org_name', announcement['org_name'])
                announcement['image_url'] = body.get(
                    'image_url', announcement['image_url'])

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
