## Notification Service

### *api_url* : `https://100092.pythonanywhere.com/notification/notification/`

- *POST*


    - Request Body

    ```json
    {
            "username": "<username>",
            "portfolio": "<portfolio name>",
            "productName": "<product name>",
            "companyId": "<company_id>",
            "orgName": "<org name>",
            "title": "<Notification title>",
            "message": "<Message>",
            "link": "<if any link or dont post>",
            "duration": "<time duration or type no limit",
            "seen": false
    }

    ```

    - Response 201

    ```json
    {
            "id": 1,
            "username": "<username>",
            "portfolio": "<portfolio name>",
            "productName": "<product name>",
            "companyId": "<company_id>",
            "orgName": "<org name>",
            "title": "<Notification title>",
            "message": "<Message>",
            "link": "<if any link or dont post>",
            "duration": "<time duration or type no limit",
            "seen": false
        },
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
            "id": 1,
            "username": "<username>",
            "portfolio": "<portfolio name>",
            "productName": "<product name>",
            "companyId": "<company_id>",
            "orgName": "<org name>",
            "title": "<Notification title>",
            "message": "<Message>",
            "link": "<if any link or dont post>",
            "duration": "<time duration or type no limit",
            "seen": false
        },
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
    "seen": "<True>"
    }
    ```

    - Response 201

    ```json
    {
            "id": 1,
            "username": "<username>",
            "portfolio": "<portfolio name>",
            "productName": "<product name>",
            "companyId": "<company_id>",
            "orgName": "<org name>",
            "title": "<Notification title>",
            "message": "<Message>",
            "link": "<if any link or dont post>",
            "duration": "<time duration or type no limit",
            "seen": true
        },
    ```

    - Response 400

    ```json
    {
        {"message":"serializer.errors"},status=400
    }
    ```