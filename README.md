# Quizz Night Service

## Usage

All responses will have the form:

- On success 
```json
{
  "result": {
    "data": "Mixed type holding the content of the response"
  },
  "success": true,
  "errors": null
}
```
- On failure
```json
{
  "result": null,
  "success": true,
  "errors": {
    "id": "0001",
    "message": "Invalid Field(s)"
  }
}
```

## Endpoints

`/players` [endpoint reference](docker/players/README.md)
`/teams` [endpoint reference](docker/teams/README.md)

