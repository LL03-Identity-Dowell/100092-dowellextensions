from django.http import JsonResponse
from utils.general import logger
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import status
from .serializers import AnnouncementSerializer
from utils.dowell_db_call import (
    fetch_document,
    ANNOUNCEMENT_COLLECTION
)
import json


def health(request):
    return JsonResponse({"Status": "OK"})

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
        
