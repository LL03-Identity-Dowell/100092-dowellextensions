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





class OldFavouritesView(APIView):
    def get(self,request, username):
        # username = request.data.get('username', None)
        if username:
            try:
                favourites = favourite.objects.filter(username = username)
                serializer = favouriteSerializer(favourites, many=True)
                return Response(serializer.data)
            except favourite.DoesNotExist:
                return Response({"message":"Not Found"}, status=status.HTTP_404_NOT_FOUND)
        return Response({'message': 'all fields required'}, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name='dispatch')
class Oldfavourite(APIView):
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
    
    def delete(self, request, pk, format=None):
        try:
            snippet = self.get_object(pk)
            snippet.delete()
            return Response([],status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"message": "no data"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 


class FavouritesView(APIView):
    def get(self,request):
        try:
            response = fetch_document(
                FAVORITE_COLLECTION,
                fields={
                    "favorite.type":"favorite",
                    "favorite.deleted": False
            })
        
            return Response(response)
        except Exception as e:
            logger.error(f"Favorite not found, {str(e)}")
            Response(
                {"message": f"Favorite not found, {str(e)}"},
                status=status.HTTP_404_NOT_FOUND)
            

    def post(self, request):
        try:
            data = request.data
            print(data)
            serializer = favouriteSerializer(data=data)
            if serializer.is_valid():
                response = serializer.save()
                return Response(response, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error Setting Favorite ({str(e)})")
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
            
class FavouritesByUserIdView(APIView):
    def get(self,request, user_id):
        try:
            response = fetch_document(
                FAVORITE_COLLECTION,
                fields={
                    "favorite.type":"favorite",
                    "favorite.deleted": False,
                    "favorite.user_id":user_id
            })
        
            return Response(response)
        except Exception as e:
            logger.error(f"Favorite not found, {str(e)}")
            Response(
                {"message": f"Favorite not found, {str(e)}"},
                status=status.HTTP_404_NOT_FOUND)


@method_decorator(csrf_exempt, name='dispatch')
class setasfavourite(APIView):
    def get(self, request,pk, format=None):
        try:
            response = fetch_document(
                FAVORITE_COLLECTION,
                fields={
                    "favorite.type":"favorite",
                    "favorite.deleted": False,
                    "_id": pk
            })
        
            return Response(response)
        except Exception as e:
            logger.error(f"Bad request, {str(e)}")
            Response(
                {"message": f"Bad request, {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST)
    

    def put(self, request, pk, format=None):
        try:
            body = json.loads(request.body)
            response = fetch_document(
                collection=FAVORITE_COLLECTION,
                fields={
                    "_id": pk,
                    "favorite.deleted": False,
                    "favorite.type": "favorite"
                },
            )

            if response["isSuccess"] and response['data']:
                favorite = response["data"][0]['favorite']
                favorite["image_url"] = body["image_url"]
                favorite["product_name"] = body["product_name"]
                favorite["product_id"] = body["product_id"]
                favorite["org_id"] = body["org_id"]
                favorite["org_name"] = body["org_name"]
                favorite["portfolio"] = body["portfolio"]

                response = favouriteSerializer.update(pk, favorite)
            else:
                logger.error(f"Favorite Not Found For {id}")
                return Response(
                    {"message": f"Favorite Not Found For {id}"},
                    status=status.HTTP_404_NOT_FOUND)
            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            logger.error(str(e))
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
    def delete(self, request, pk, format=None):
        try:
            response = fetch_document(
                collection=FAVORITE_COLLECTION,
                fields={
                    "_id": pk,
                    "favorite.deleted": False,
                    "favorite.type": "favorite"
                },
            )

            if response["isSuccess"] and response['data']:
                favorite = response["data"][0]['favorite']
                favorite['deleted'] = not favorite['deleted']
                response = favouriteSerializer.update(pk, favorite)
            else:
                logger.error(f"Favorite Not Found For {id}")
                return Response(
                    {"message": f"Favorite Not Found For {id}"},
                    status=status.HTTP_404_NOT_FOUND)
            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            logger.error(str(e))
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

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




class FavouriteImageList(APIView):
    def get(self, request, user_id, format=None):
        try:
            response_json = fetch_document(
                collection=FAVORITE_COLLECTION,
                fields={
                    "favorite.user_id": user_id,
                    "favorite.type": "favorite-image",
                    "favorite.deleted": False
                }
            )

            return Response(response_json)

        except Exception as e:
            logger.error(f"Bad Request, {str(e)}")
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, user_id):
        try:
            data = request.data
            data["user_id"] = user_id

            serializer = ImageSerializer(data=data)
            if serializer.is_valid():
                response = serializer.save()
                return Response(response, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            logger.error(f"Error Creating Favorite Image ({str(e)})")
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class FavouriteImageDetail(APIView):
    def get(self, request, user_id, favorite_img_id, format=None):
        try:
            response_json = fetch_document(
                collection=FAVORITE_COLLECTION,
                fields={
                    "_id": favorite_img_id,
                    "favorite.user_id": user_id,
                    "favorite.deleted": False,
                    "favorite.type": "favorite-image"
                    
                },
            )
            return Response(response_json)

        except Exception as e:
            logger.error(f"Favorite Image not found, {str(e)}")
            Response(
                {"message": f"Favorite Image not found, {str(e)}"},
                status=status.HTTP_404_NOT_FOUND)

    def put(self, request, user_id, favorite_img_id, format=None):


        try:
            body = json.loads(request.body)
            response = fetch_document(
                collection=FAVORITE_COLLECTION,
                fields={
                    "_id": favorite_img_id,
                    "favorite.user_id": user_id,
                    "favorite.deleted": False,
                    "favorite.type": "favorite-image"
                },
            )

            if response["isSuccess"] and response['data']:
                favorite = response["data"][0]['favorite']
                favorite['image_url'] = body['image_url']
                response = ImageSerializer.update(favorite_img_id, favorite)
            else:
                logger.error(f"Favorite Image Not Found For {id}")
                return Response(
                    {"message": f"Favorite Image Not Found For {id}"},
                    status=status.HTTP_404_NOT_FOUND)
            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            logger.error(str(e))
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, user_id, favorite_img_id, format=None):
        try:
            response = fetch_document(
                collection=FAVORITE_COLLECTION,
                fields={
                    "_id": favorite_img_id,
                    "favorite.user_id": user_id,
                    "favorite.deleted": False,
                    "favorite.type": "favorite-image"
                },
            )

            if response["isSuccess"] and response['data']:
                favorite = response["data"][0]['favorite']
                favorite['deleted'] = not favorite['deleted']
                response = ImageSerializer.update(favorite_img_id, favorite)
            else:
                logger.error(f"Favorite Image Not Found For {id}")
                return Response(
                    {"message": f"Favorite Image Not Found For {id}"},
                    status=status.HTTP_404_NOT_FOUND)
            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            logger.error(str(e))
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
