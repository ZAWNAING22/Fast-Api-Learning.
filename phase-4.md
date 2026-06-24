## Request Body

A **Request Body** is the data that a client sends to your API.

Think of it like filling out a form and sending it to a server.

For example, when creating a new user:

```http
POST /users
```

Client sends:

```json
{
  "name": "John",
  "age": 25
}
```

This JSON data is the **request body**.

---

## Why do we need it?

Imagine a food delivery app.

When a user places an order, the app must send:

```json
{
  "food": "Pizza",
  "quantity": 2,
  "address": "123 Main St"
}
```

Without a request body, the server wouldn't know what the user wants.

---

## What is Pydantic?

**Pydantic** is a Python library used by FastAPI to:

* Define the structure of data
* Validate input automatically
* Convert data types when possible

FastAPI heavily relies on Pydantic.

---

## Pydantic Model

A Pydantic model is a class that describes what data should look like.

Example:

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
```

This says:

* `name` must be a string
* `age` must be an integer

---

## Using it in FastAPI

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.post("/users")
def create_user(user: User):
    return user
```

---

### Request

```json
{
  "name": "John",
  "age": 25
}
```

### Response

```json
{
  "name": "John",
  "age": 25
}
```

FastAPI automatically:

1. Reads JSON
2. Creates a `User` object
3. Validates data
4. Passes it to your function

---

## Input Validation

Validation means checking if the data is correct before processing it.

### Valid Request

```json
{
  "name": "John",
  "age": 25
}
```

✅ Accepted

---

### Invalid Request

```json
{
  "name": "John",
  "age": "twenty five"
}
```

❌ Rejected

FastAPI returns:

```json
{
  "detail": [
    {
      "msg": "Input should be a valid integer"
    }
  ]
}
```

Because `age` must be an integer.

---

## Required vs Optional Fields

Required:

```python
class User(BaseModel):
    name: str
    age: int
```

Both fields are mandatory.

---

Optional:

```python
from typing import Optional

class User(BaseModel):
    name: str
    age: int
    email: Optional[str] = None
```

Now `email` can be omitted.

---

## More Validation Rules

```python
from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    age: int = Field(gt=0, lt=120)
```

Meaning:

* Name must be 2–50 characters
* Age must be greater than 0
* Age must be less than 120

---

### Invalid Example

```json
{
  "name": "A",
  "age": -5
}
```

❌ Validation error

---

## Real-World Example

### User Registration API

```python
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class RegisterUser(BaseModel):
    username: str
    email: EmailStr
    password: str

@app.post("/register")
def register(user: RegisterUser):
    return {
        "message": "User registered",
        "user": user
    }
```

Request:

```json
{
  "username": "john",
  "email": "john@gmail.com",
  "password": "123456"
}
```

FastAPI checks:

* Username exists
* Email format is valid
* Password field exists

before running the function.

---

## Mental Model

When a client sends data:

```json
{
  "name": "John",
  "age": 25
}
```

Flow:

```text
Client
   │
   ▼
JSON Request Body
   │
   ▼
Pydantic Model (User)
   │
   ├─ Valid? ──► Yes ──► Function runs
   │
   └─ Invalid? ─► FastAPI returns error
```

### What you should remember

* **Request Body** = data sent to the API (usually JSON).
* **Pydantic Model** = blueprint describing what data should look like.
* **Input Validation** = checking incoming data is correct.
* FastAPI automatically validates data using Pydantic before your code runs.

This topic is one of the most important in FastAPI because almost every real backend API (login, registration, orders, ML predictions, task managers, etc.) receives data through request bodies and validates it with Pydantic models.
