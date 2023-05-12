## Announcement Services

_api_url_ : `https://100092.pythonanywhere.com/announcement/`

- _POST_

  - Request Body

  ```json
  {
    "description": "Hello World",
    "product": "WorkFlow",
    "created_by": "Manish",
    "member_type": "Public | Member | User",
    "company_id": "sahjg272346",
    "created_at_position": "Platform Admin"
  }
  ```

  _Note_ : every field is mandatory

  - Response 201 Created

  ```json
  {
    "id": 1,
    "description": "Hello World",
    "created_at": "2023-05-11T07:56:03.043295Z",
    "product": "WorkFlow",
    "created_by": "fazzie",
    "is_active": true,
    "member_type": "workflow",
    "company_id": "sahjg272346",
    "created_at_position": "admin"
  }
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
  [
    {
      "id": 1,
      "description": "updated hello world",
      "created_at": "2023-05-11T07:56:03.043295Z",
      "product": "WorkFlow",
      "created_by": "fazzie",
      "is_active": true,
      "member_type": "updated member type",
      "company_id": "sahjg272346",
      "created_at_position": "admin"
    }
  ]
  ```

- _PUT_ to `/<int:pk>`

  - Response 200

  ```json
  {
    "id": 4,
    "description": "Hello World",
    "created_at": "2023-05-11T07:35:12.077955Z",
    "product": "WorkFlow",
    "created_by": "fazzie",
    "is_active": false,
    "member_type": "djfdj",
    "company_id": "djjsdhf",
    "created_at_position": "jdfhjdfhjdhfdj"
  }
  ```

  _Note_ : put does not require request body. It changes the is_active field to false

  - Response 404

  ```json
  {
    "detail": "Not found."
  }
  ```

- _PATCH_ to `/<int:pk>`

  - Request Body

  ```json
  {
    "description": "updated hello world",
    "member_type": "updated member type"
  }
  ```

  _Note_ : patch is partial update

  - Response 200 OK

  ```json
  {
    "id": 1,
    "description": "updated hello world",
    "created_at": "2023-05-11T07:56:03.043295Z",
    "product": "WorkFlow",
    "created_by": "fazzie",
    "is_active": true,
    "member_type": "updated member type",
    "company_id": "sahjg272346",
    "created_at_position": "admin"
  }
  ```
