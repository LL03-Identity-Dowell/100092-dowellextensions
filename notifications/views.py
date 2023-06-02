from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, generics
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
from django.http import Http404
from utils.general import logger
from utils.dowell_db_call import (
    fetch_document,
    update_document,
    NOTIFICATION_COLLECTION
    )


class ProductNotificationList(APIView):
    """
        Retreive and Create new notification
    """
    def get(self, request, format=None):
        try:
            # Retrieve all records
            response_json = fetch_document(
                collection=NOTIFICATION_COLLECTION,
                fields={
                    "notification.document_type": "product_notification",
                    "notification.deleted": False
                },
            )
            return Response(response_json)
        
        except Exception as e:
            logger.error(f"Bad Request, {str(e)}")
            Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    
    def post(self, request):
        try:

            data = request.data
            serializer = ProductNotificationSerializer(data=data)
            if serializer.is_valid():
                response = serializer.save()
                return Response(response, status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            logger.error(str(e))
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class ProductNotificationDetail(APIView):
    def get(self, request, document_id, format=None):
        try:
            # Retrieve record
            response_json = fetch_document(
                collection=NOTIFICATION_COLLECTION,
                fields={
                    "notification.document_type": "product_notification",
                    "notification.document_id": document_id,
                    "notification.deleted": False
                },
            )
            return Response(response_json)
        
        except Exception as e:
            logger.error(f"Product notification not found, {str(e)}")
            Response(
                {"message": f"Product notification not found, {str(e)}"},
                  status=status.HTTP_404_NOT_FOUND)


    def patch(self, request, document_id, format=None):
        try:
            # Retrieve record
            response = fetch_document(
                collection=NOTIFICATION_COLLECTION,
                fields={
                    "notification.document_type": "product_notification",
                    "notification.document_id": document_id,
                    "notification.deleted": False
                },
            )

            if response["isSuccess"] and response['data']:
                notification = response["data"][0]['notification']
                notification['seen'] = True
                notification['seen_at'] = datetime.utcnow().isoformat()
                # Save record
                response = ProductNotificationSerializer.patch(document_id, notification)

            else:
                logger.error(f"Notitication Not Found For {document_id}")
                return Response(
                    {"message": f"Notitication Not Found For {document_id}"}, 
                    status=status.HTTP_404_NOT_FOUND)

            return Response(response, status=status.HTTP_200_OK)
        
        except Exception as e:
            logger.error(str(e))
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def delete(self, request, document_id, format=None):
        try:
            # Retrieve record
            response = fetch_document(
                collection=NOTIFICATION_COLLECTION,
                fields={
                    "notification.document_type": "product_notification",
                    "notification.document_id": document_id,
                    "notification.deleted": False
                },
            )

            if response["isSuccess"] and response['data']:
                notification = response["data"][0]['notification']
                notification['deleted'] = True
                # Save record
                response = ProductNotificationSerializer.patch(document_id, notification)

            else:
                logger.error(f"Notitication Not Found For {document_id}")
                return Response(
                    {"message": f"Notitication Not Found For {document_id}"}, 
                    status=status.HTTP_404_NOT_FOUND)

            return Response(response, status=status.HTTP_200_OK)
        
        except Exception as e:
            logger.error(str(e))
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class NotificationList(generics.ListCreateAPIView):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        org_id = self.request.query_params.get('org_id', None)
        if org_id is None:
            return Notification.objects.none()
        queryset = Notification.objects.filter(org_id=org_id)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NotificationDetail(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def get_queryset(self):
        org_id = self.request.query_params.get('org_id', None)
        return Notification.objects.filter(org_id=org_id)

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.first()
        if not obj:
            raise Http404(
                "Notification does not exist or does not belong to the organization.")
        return obj

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = NotificationSerializer(
            instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
