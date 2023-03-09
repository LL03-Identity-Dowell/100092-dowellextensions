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
        "title": "<Notification title>",
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
        "title": "<Notification title>",
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
        "title": "<Notification title>",
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
        "title": "<Notification title>",
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
