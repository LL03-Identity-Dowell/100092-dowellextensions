import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.views import APIView
from database.connection import dowellconnection
from database.event import get_event_id
from database.database_management import notification_details

@method_decorator(csrf_exempt, name='dispatch')
class serverStatus(APIView):

    def post(self, request):
        return Response({"info": "Welcome to Dowell-Job-Portal-Version2.0"},status=status.HTTP_200_OK)
    

@method_decorator(csrf_exempt, name='dispatch')
class notification(APIView):
    def get_object(self, pk):
        try:
            return Noftification.objects.get(pk=pk)
        except Noftification.DoesNotExist:
            return Response({"message":"Not Found"}, status=status.HTTP_404_NOT_FOUND)
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
    
    def patch(self, request, pk, format=None):
        Notification = self.get_object(pk)
        Notification.seen = True
        Notification.save()
        return Response({"message": "success"}, status=status.HTTP_200_OK)
    
    # def patch(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     snippet.seen = True
    #     snippet.save()
    #     serializer = sendProductNotificationSerializer(snippet, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(snippet, status=status.HTTP_400_BAD_REQUEST)
   