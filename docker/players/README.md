# Quizz Night Service

## /players endpoint

**Fields of each Player**

`"username":string` - required, unique
`"display_name":string` - required, unique
`"team_name":string` 

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
      "team_name": "goshkovci"
    },
    {
      "username": "pesho",
      "display_name": "Pesho Peshev",
      "team_name": "peshkovci"
    }
  ],
  "success": true,
  "errors": null
}
```

### List a single player 

**Definition**

`GET /players/<username>`

**Response**

`200 OK` on success. When the player exists

```json
{
  "result": {
    "username": "ivan",
    "display_name": "Ivan",
    "team_name": "goshkovci"
  },
  "success": true,
  "errors": null
}
```

`404 Not Found` on failure. When the player does not exist

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
- `"team_name":string` - optional

**Response**

`200 OK` on success. The Player ID will be assigned automatically on registration. 

```json
{
  "result": {
    "username": "gosho",
    "name": "Gergi",
    "team_name": "goshkovci"
  },
  "success": true,
  "errors": null
}
```

`400 Bad Request` on failure. When the player already exists

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
- `"team_name":string` 

**Response**

`200 OK` on success. The updated Player will be returned

```json
{
  "result": {
    "username": "pesho",
    "name": "Pesho",
    "team_name": "peshkovci"
  },
  "success": true,
  "errors": null
}
```

`400 Bad Request` on failure. When the Player does not exist or the username/display_name is already taken

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

`DELETE /players/<username>`

**Response**

`200 OK` on success. When the player has been deleted successfully

```json
{
  "result": null,
  "success": true,
  "errors": null
}
```

`404 Not Found` on failure. When the Player does not exist
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
