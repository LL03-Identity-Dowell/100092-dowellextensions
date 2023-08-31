from rest_framework.response import Response
from .serializers import DowellGroupSerializer
from utils.general import logger
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.views import APIView
from utils.dowell_db_call import (
    fetch_document,
    DOWELL_GROUP_COLLECTION
)
import json

class DowellGroupList(APIView):
    def get(self, request, format=None):
        try:
            params = request.query_params
            if "user_id" not in params:
                return Response({"message": "Missing parameter 'user_id'"}, status=status.HTTP_400_BAD_REQUEST)
             
            response_json = fetch_document(
                collection=DOWELL_GROUP_COLLECTION,
                fields={
                    "DowellGroup.user_id": params['user_id'],
                    "DowellGroup.deleted": False
                }
            )
            return Response(response_json)
        except Exception as e:
            logger.error(f"Bad Request, {str(e)}")
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


    def post(self, request):
        try:
            data = request.data
            serializer = DowellGroupSerializer(data=data)
            if serializer.is_valid():
                response = serializer.save()
                return Response(response, status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(str(e))
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class DowellGroupDetail(APIView):
    def get(self, request, group_id, format=None):
        try:
            response_json = fetch_document(
                collection=DOWELL_GROUP_COLLECTION,
                fields={
                    "_id": group_id
                },
            )
            return Response(response_json)

        except Exception as e:
            logger.error(f"Group not found, {str(e)}")
            Response(
                {"message": f"Group not found, {str(e)}"},
                status=status.HTTP_404_NOT_FOUND)

    def put(self, request, group_id, format=None):
        try:
            body = json.loads(request.body)
            response = fetch_document(
                collection=DOWELL_GROUP_COLLECTION,
                fields={
                    "_id": group_id
                },
            )

            if response["isSuccess"] and response['data']:
                dowellgroup = response["data"][0]['DowellGroup']
                dowellgroup['group_name'] = body['group_name']
                dowellgroup['org_id'] = body['org_id']
                dowellgroup['org_name'] = body['org_name']
                dowellgroup['email_list'] = body['email_list']
                response = DowellGroupSerializer.update(group_id, dowellgroup)

            else:
                logger.error(f"Group Not Found For {id}")
                return Response(
                    {"message": f"Group Not Found For {id}"},
                    status=status.HTTP_404_NOT_FOUND)

            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            logger.error(str(e))
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def delete(self, request, group_id, format=None):
        try:
            response = fetch_document(
                collection=DOWELL_GROUP_COLLECTION,
                fields={
                    "_id": group_id
                },
            )

            if response["isSuccess"] and response['data']:
                dowellgroup = response["data"][0]['DowellGroup']
                dowellgroup['deleted'] = not dowellgroup['deleted']
                response = DowellGroupSerializer.update(group_id, dowellgroup)

            else:
                logger.error(f"Group Not Found For {id}")
                return Response(
                    {"message": f"Group Not Found For {id}"},
                    status=status.HTTP_404_NOT_FOUND)

            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            logger.error(str(e))
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)