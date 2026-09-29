from jsonschema import validate

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "number"}
    },
    "required": ["name"]
}

data = {
    "name": "Alice",
    "age": 30
}

validate(instance=data, schema=schema)

# массив
schema = {
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "id": { "type": "string" },
      "value": { "type": "number" }
    },
    "required": ["id", "value"]
  }
}

# Строка ограниченная по длине
schema = {
  "type": "object",
  "properties": {
    "username": {
      "type": "string",
      "minLength": 3,
      "maxLength": 20
    }
  },
  "required": ["username"]
}

# Рег выр-е для валидации имейла
schema = {
  "type": "object",
  "properties": {
    "email": {
      "type": "string",
      "pattern": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"
    }
  },
  "required": ["email"]
}



