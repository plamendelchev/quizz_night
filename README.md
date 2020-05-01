# Quizz Night Service

## Usage

All responses will have the form
```json
{
  "result": {
    "data": "Mixed type holding the content of the response"
  },
  "success": true,
  "errors": {
		"id": "0001",
		"message": "Invalid Field(s)"
  }
}
```

### List all Players

**Definition**

`GET /players`

**Response**

- `200 OK` on success

```json
{
  "result": [
     {
       "username": "gosho",
       "display_name": "Gosho Goshev",
       "team_id": 5
     },
     {
       "username": "pesho",
       "display_name": "Pesho Peshev",
       "team_id": 3
     }
   ],
  "success": true,
  "errors": null
}
```

### List player details

**Definition**

`GET /players/<id>`

**Response**

`200 OK` When the player exists

```json
{
  "result": {
    "username": "ivan",
    "display_name": "Ivan",
    "team_id": 2
  },
  "success": true,
  "errors": null
}
```

`404 Not Found` When the player does not exist

```json
{
  "result": null,
  "success": false,
  "errors": {
		"id": "0003",
		"message": "Player does not exist"
  }
}
```

### Registering a new Player

**Definition**

`POST /players`

**Arguments**

- `"username":string` 
- `"display_name":string` 

The Player ID will be assigned automatically on registration. 

**Response**

`200 OK` When the player has been registered successfully

```json
{
  "result": {
    "username": "gosho",
    "name": "Gergi",
    "team_id": 5
  },
  "success": true,
  "errors": null
}
```

`400 Bad Request` When the player already exists

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

### Modifying a new Player

**Definition**

`PATCH /players/<username>`

**Arguments**

- `"username":string` 
- `"display_name":string` 

**Response**

`200 OK` When the player has been registered modified. The new player information will be returned

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

`400 Bad Request` When the player does not exist or the username/display_name is already taken

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

### Deleting a Player

**Definition**

`DELETE /players/<id>`

**Response**

`200 OK` When the player has been deleted successfully

```json
{
  "result": null,
  "success": true,
  "errors": null
}
```

`404 Not Found` When the Player ID does not exist
```json
{
  "result": null,
  "success": false,
  "errors": {
		"id": "0003",
		"message": "Player does not exist"
  }
}
```
