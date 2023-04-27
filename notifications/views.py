import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, generics
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
from database.connection import dowellconnection
from database.event import get_event_id
from database.database_management import notification_details
from django.http import Http404


@method_decorator(csrf_exempt, name='dispatch')
class serverStatus(APIView):

    def post(self, request):
        return Response({"info": "Welcome to Dowell-Job-Portal-Version2.0"}, status=status.HTTP_200_OK)


@method_decorator(csrf_exempt, name='dispatch')
class notification(APIView):
    def get_object(self, document_id):
        try:
            return Noftification.objects.get(document_id=document_id)
        except Noftification.DoesNotExist:
            return Response({"message": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        data = request.data
        serializer = sendProductNotificationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        snippets = Noftification.objects.all()
        serializer = sendProductNotificationSerializer(snippets, many=True)
        return Response(serializer.data)

    def patch(self, request, document_id, format=None):
        Notification = self.get_object(document_id)
        Notification.seen = True
        Notification.save()
        return Response({"message": "success"}, status=status.HTTP_200_OK)

    def delete(self, request, document_id, format=None):
        try:
            Notification = self.get_object(document_id)
            Notification.delete()
            return Response([], status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"message": "no data"}, status=status.HTTP_404_NOT_FOUND)


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
