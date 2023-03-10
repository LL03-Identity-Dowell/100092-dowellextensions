import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from rest_framework import viewsets
from .models import *
from urllib.request import urlopen
from .serializers import *
from rest_framework.views import APIView
from PIL import Image as PILImage


@method_decorator(csrf_exempt, name='dispatch')
class setasfavourite(APIView):
    def get_object(self, pk):
        try:
            return favourite.objects.get(pk=pk)
        except favourite.DoesNotExist:
            return Response({"message":"Not Found"}, status=status.HTTP_404_NOT_FOUND)
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
   