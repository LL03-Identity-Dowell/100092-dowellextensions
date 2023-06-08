from rest_framework.response import Response
from rest_framework import generics
from .models import Announcement
from .serializers import AnnouncementSerializer
from utils.general import logger
from rest_framework import status
from rest_framework.views import APIView
from utils.dowell_db_call import (
    save_document,
    update_document,
    fetch_document,
    ANNOUNCEMENT_COLLECTION
)
import json


class AnnouncementList(APIView):
    """
        Retreive and Create new announcement list
    """

    def get(self, request, format=None):
        try:
            # Retrieve all records
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
            # Retrieve record
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
            # body = json.loads(request.body)
            # Retrieve record
            response = fetch_document(
                collection=ANNOUNCEMENT_COLLECTION,
                fields={
                    "_id": id
                },
            )

            if response["isSuccess"] and response['data']:
                announcement = response["data"][0]['announcement']
                announcement['is_Active'] = False
                # announcement['member_type'] = request.body.
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
            # Retrieve record
            response = fetch_document(
                collection=ANNOUNCEMENT_COLLECTION,
                fields={
                    "_id": id
                },
            )

            if response["isSuccess"] and response['data']:
                announcement = response["data"][0]['announcement']
                # Update the announcement object if the corresponding value is present in the body
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

                # announcement['member_type'] = request.body.
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

    # def delete(self, request, document_id, format=None):
    #     try:
    #         # Retrieve record
    #         response = fetch_document(
    #             collection=ANNOUNCEMENT_COLLECTION,
    #             fields={
    #                 "_id": id
    #             },
    #         )

    #         if response["isSuccess"] and response['data']:
    #             announcement = response["data"][0]['announcement']
    #             announcement['is_Active'] = False
    #             # Save record
    #             response = AnnouncementSerializer.patch(
    #                 announcement)

    #         else:
    #             logger.error(f"Announcement Not Found For {id}")
    #             return Response(
    #                 {"message": f"Announcement Not Found For {id}"},
    #                 status=status.HTTP_404_NOT_FOUND)

    #         return Response(response, status=status.HTTP_200_OK)

    #     except Exception as e:
    #         logger.error(str(e))
    #         return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# class AnnouncementListCreateView(generics.ListCreateAPIView):
#     queryset = Announcement.objects.filter(is_active=True)
#     serializer_class = AnnouncementSerializer


# class AnnouncementRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Announcement.objects.filter(is_active=True)
#     serializer_class = AnnouncementSerializer

#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.is_active = False
#         instance.save()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)

#     def patch(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(
#             instance, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
