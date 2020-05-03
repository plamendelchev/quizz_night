# Quizz Night Service

## /teams endpoint

**Fields of each Team**

- `"name":string` - required, unique
- `"display_name":string` - required, unique
- `"players":array`

### List all Teams

**Definition**

`GET /teams`

**Response**

- `200 OK` on success

```json
{
  "result": [
    {
      "name": "packovci",
      "display_name": "Otbora na Paco",
      "players": [
        {
          "username": "paco",
          "display_name": "Packo"
        },
        {
          "username": "mitko",
          "display_name": "Mitku"
        }
      ]
    },
    {
      "name": "goshkovci",
      "display_name": "Otbora na Gosho",
      "players": [
        {
          "username": "gosho",
          "display_name": "Goshko"
        },
        {
          "username": "misho",
          "display_name": "Mishko"
        }
      ]
    }
  ],
  "success": true,
  "errors": null
}
```

### List a single Team

**Definition**

`GET /teams/<name>`

**Response**

- `200 OK` on success

```json
{
  "result": {
    "name": "packovci",
    "display_name": "Otbora na Paco",
    "players": [
      {
        "username": "paco",
        "display_name": "Packo"
      },
      {
        "username": "mitko",
        "display_name": "Mitku"
      }
    ]
  },
  "success": true,
  "errors": null
}
```

- `404 Not Found` on failure. When the team does not exist

```json
{
  "result": null,
  "success": false,
  "errors": {
    "id": "0003",
    "message": "Team does not exist"
  }
}
```

### Registering a new Team

**Definition**

`POST /teams`

**Arguments**

- `"name":string` 
- `"display_name":string` 
- `"players":array` - optional


**Response**

- `200 OK` on success. The Team ID will be assigned automatically. 

```json
{
  "result": {
    "name": "packovci",
    "display_name": "Otbora na Paco",
    "players": [
      {
        "username": "paco",
        "display_name": "Packo"
      },
      {
        "username": "mitko",
        "display_name": "Mitku"
      }
    ]
  },
  "success": true,
  "errors": null
```

- `400 Bad Request` on failure. When the player already exists

```json
{
  "result": null,
  "success": false,
  "errors": {
    "id": "0002",
    "message": "Player already exists"
  }
}
```

### Modifying a Team

**Definition**

`PATCH /teams/<name>`

**Arguments**

- `"username":string` 
- `"display_name":string` 
- `"players":array` - optional

**Response**

- `200 OK` on success. The updated team will be returned

```json
{
  "result": {
    "username": "pesho",
    "name": "Pesho",
    "team_id": 5
  },
  "success": true,
  "errors": null
}
```

- `400 Bad Request` on failure. When the player does not exist or the name/display_name is already taken

```json
{
  "result": null,
  "success": false,
  "errors": {
    "id": "0002",
    "message": "Team already exists"
  }
}
```

### Deleting a Team

**Definition**

`DELETE /teams/<username>`

**Response**

- `200 OK` on success. When the Team has been deleted successfully

```json
{
  "result": null,
  "success": true,
  "errors": null
}
```

- `404 Not Found` on failure. When the Team does not exist
```json
{
  "result": null,
  "success": false,
  "errors": {
    "id": "0003",
    "message": "Team does not exist"
  }
}
```
