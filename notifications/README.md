## Notification Service

_api_url_ : `https://100092.pythonanywhere.com/notification/notification/`

- _POST_

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
    "seen": false,
    "document_id": "<document_id>",
    "button_status": "title"
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

- _GET_

  - Response 200

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
          "seen": false,
          "button_status": "title",
          "document_id": "id"
      },
  ```

  - Response 400

  ```json
  {
      {"message":"serializer.errors"},status=400
  }
  ```

- _PATCH_ to `/<int:document_id>`

  - Response 200

  ```json
  {"message": "success"},
  ```

  - Response 404

  ```json
  { "message": "Not Found" }
  ```

- _DELETE_ to `/<int:document_id>`

  - Response 204

  ```json
  []
  ```

  - Response 404

  ```json
  { "message": "Not Found" }
  ```
