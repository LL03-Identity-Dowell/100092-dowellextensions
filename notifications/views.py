import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from database.connection import dowellconnection
from database.event import get_event_id
from database.database_management import notification

@method_decorator(csrf_exempt, name='dispatch')
class serverStatus(APIView):

    def post(self, request):
        return Response({"info": "Welcome to Dowell-Job-Portal-Version2.0"},status=status.HTTP_200_OK)
    

@method_decorator(csrf_exempt, name='dispatch')
class testdatabase(APIView):
    def post(self, request):
            name = request.GET.get('name',None)
            lastname = request.GET.get('lastname',None)
            field = {
                 "evenId":get_event_id()['event_id'],
                 "name":name,
                 "lastname":lastname
                }
            update_field = {
                "status":"nothing to update"
            }
        
            insert_response = dowellconnection(*notification,"insert",field,update_field)
            print(insert_response)
            if insert_response :
                return Response({"message":"ok"},status=status.HTTP_200_OK)
            else:
                return Response({"message":"ok"},status=status.HTTP_304_NOT_MODIFIED)
        
"""
{
username
portfolio
product name
org name
title
message
link(koi link hai toh)
seen = False
}
// TODO:
- psot by product people(local db)
- get by extenion people
- when seen flag turns to "true" then 
    - update to local db
    - insert to mongodb using dowell connection
"""