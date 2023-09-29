import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.views import APIView
import imghdr
from utils.general import logger
from utils.dowell_db_call import (
    fetch_document,
    FAVORITE_COLLECTION
)
import json


class FavouritesView(APIView):
    def get(self,request, username):
        try:
            response = fetch_document(
                FAVORITE_COLLECTION,
                fields={
                    "username":username
            })
        
            return Response(response)
        except Exception as e:
            logger.error(f"Favorite not found, {str(e)}")
            Response(
                {"message": f"Favorite not found, {str(e)}"},
                status=status.HTTP_404_NOT_FOUND)


@method_decorator(csrf_exempt, name='dispatch')
class setasfavourite(APIView):
    def get_object(self, pk):
        try:
            response = fetch_document(
                FAVORITE_COLLECTION,
                fields={
                    "_id":pk
            })
            return Response(response)

        except Exception as e:
            logger.error(f"Favorite not found, {str(e)}")
            Response(
                {"message": f"Favorite not found, {str(e)}"},
                status=status.HTTP_404_NOT_FOUND)
    def post(self, request):
        data = request.data.copy()
        if 'image' in data and data['image']:
            serializer = favouriteSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            product = data['productName']
            import json
            # Open the JSON file
            with open('favourite/favourite.json') as f:
                # Load the JSON data into a Python dictionary
                json_data = json.load(f)
                # print(json_data)
            # Get the values from the dictionary and put them in a list
            for i in json_data:
                if product == i['title']:
                    image_url = i['image']
                    print(image_url)
            data['image_url'] = image_url
            
 
            serializer = favouriteSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def get(self, request, format=None):
        snippets = favourite.objects.all()
        serializer = favouriteSerializer(snippets, many=True)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        data = request.data
        snippet.save()
        serializer = favouriteSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(snippet, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        try:
            snippet = self.get_object(pk)
            snippet.delete()
            return Response([],status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"message": "no data"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

@method_decorator(csrf_exempt, name='dispatch')
class favouriteIcon(APIView):
    def get(self, request):
        with open('/home/100092/100092-dowellextensions/favourite/favouriteIcons.json') as f:
            json_data = json.load(f)
            return Response(json_data)
        

@method_decorator(csrf_exempt, name='dispatch') 
class FavouriteImageView(APIView):
    def post(self, request):
        image = request.data.get('image', None)
        username = request.data.get('username', None)
        session_id = request.data.get('session_id', None) 

        if image and username and session_id:
            if not type(image) == str:
                image_data = image.read()
                image_data_base64 = base64.b64encode(image_data)
                image_data_base64_string = image_data_base64.decode('utf-8')
                image_format = imghdr.what(None, image_data)
                image_data_base64_string = f"data:image/{image_format};base64,{image_data_base64_string}"
                request.data['image'] = image_data_base64_string
            serializer = ImageSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'all fields required'}, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, username):
        try:
            favourites = FavouriteImage.objects.filter(username = username)
            serializer = ImageSerializer(favourites, many=True)
            return Response(serializer.data)
        except favourite.DoesNotExist:
            return Response({"message":"Not Found"}, status=status.HTTP_404_NOT_FOUND)
