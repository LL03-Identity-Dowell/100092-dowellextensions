## Backend services for Extension Service

### api https://100092.pythonanywhere.com/

_Post_ to `notification/sendProductNotification/`

- if you not understand see the example end of the page

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
},

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
    {
    "message":"serializer.errors"
    },
    status=400

}
```

_get_ to `notification/sendProductNotification/`

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
    {
    "message":"serializer.errors"
    },
    status=400

}
```

_put_ to `notification/sendProductNotification/<int:pk>`

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
        "seen": false
    },
```

- Response 400

```json
{
    {
    "message":"serializer.errors"
    },
    status=400

}
```

# Extension Service

[Postman Documentation](https://documenter.getpostman.com/view/14666556/2s93JowQej) - Read the documentation

#### Note:

- Product team : _POST_ to `https://100092.pythonanywhere.com/notification/sendProductNotification/`
- Extension Team :

  - _GET_ from `https://100092.pythonanywhere.com/notification/sendProductNotification/`
  - _PUT_ to `https://100092.pythonanywhere.com/notification/putProductNotification/`
