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
        try:
            response_json = fetch_document(
                collection=ANNOUNCEMENT_COLLECTION,
                fields={
                    "announcement.is_Active": True
                },
            )
            return Response(response_json)

        except Exception as e:
            logger.error(f"Bad Request, {str(e)}")
            Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

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

    def put(self, request, id, format=None):
        try:
            response = fetch_document(
                collection=ANNOUNCEMENT_COLLECTION,
                fields={
                    "_id": id
                },
            )

            if response["isSuccess"] and response['data']:
                announcement = response["data"][0]['announcement']
                announcement['is_Active'] = False
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

    def patch(self, request, id, format=None):
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
                announcement['company_id'] = body.get(
                    'company_id', announcement['company_id'])
                announcement['created_at_position'] = body.get(
                    'created_at_position', announcement['created_at_position'])

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
