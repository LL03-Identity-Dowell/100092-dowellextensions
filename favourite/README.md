## Favourite Services
*api_url* : `https://100092.pythonanywhere.com/favourite/favourite/`

- *POST*

    - Request Body

    ```json
    {
        "username": "<username>",
        "portfolio": "<portfolio name>",
        "productName": "<product name>",
        "action": "<true or false>",
        "orgName": "<org name>",
        "image": "<uploaded image optional>",
    }

    ```
    *Note* : if you don't post anything in the image then a default image url will be returned

    - Response 201

    ```json
    {
        "id":1,
        "username": "<username>",
        "portfolio": "<portfolio name>",
        "productName": "<product name>",
        "action": "<true>",
        "orgName": "<org name>",
        "image": "<uploaded image>",
    }
    ```
    - Response 400

    ```json
    {
        {"message":"serializer.errors"},status=400
    }
    ```
- *GET*

    - Response 201

    ```json
    {
        "id":1,
        "username": "<username>",
        "portfolio": "<portfolio name>",
        "productName": "<product name>",
        "action": "<true>",
        "orgName": "<org name>",
        "image": "<uploaded image>",
    }
    ```

    - Response 400

    ```json
    {
        {"message":"serializer.errors"},status=400
    }
    ```
- *PUT* to `/<int:pk>`
    - Request Body

    ```json
    {
    "action": "<True/false>"
    <!-- add true and remove false -->
    }
    ```

    - Response 201

    ```json
    {
        "id":1,
        "username": "<username>",
        "portfolio": "<portfolio name>",
        "productName": "<product name>",
        "action": "<false>",
        "orgName": "<org name>",
        "image": "<uploaded image>",
    }
    ```

    - Response 400

    ```json
    {
        {
        {"message":"serializer.errors"},status=400
    }

    }
    ```
- *Delete* /<int:pk>
Response-204
```
[]
```
Response-500
```json
{
    "message": "no data"
}
```

# FavouriteImage
*api_url* : `https://100092.pythonanywhere.com/favourite/favouriteImage/`

- *POST*

    - Request Body

    ```json
    {
        "username": "<username>",
        "session_id": "<session_id>",
        "image": "<uploaded image optional>",
    }

    ```

    - Response 201

    ```json
    {
        "id":1,
        "username": "<username>",
        "session_id": "<session_id>",
        "image": "<uploaded image>",
    }
    ```
    - Response 400

    ```json
    {
        {"message":"serializer.errors"},status=400
    }
    ```

- *GET* to `/<str:username>`

    - Response 200

    ```json
    {
        "id":1,
        "username": "<username>",
        "session_id": "session_id",
        "image": "<uploaded image>",
    }
    ```

    - Response 404

    ```json
    {
        "message":"Not Found"
    }
    ```
