When building real FastAPI APIs, error handling usually happens in **3 layers**:

```text
Client Request
      │
      ▼
1. Pydantic Validation
      │
      ▼
2. Business Logic Checks
      │
      ▼
3. System/Database/External Errors
```

---

# 1. Pydantic Validation Errors

This is the **first defense layer**.

Before your function runs, FastAPI checks the request body.

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
```

Request:

```json
{
  "name": "John",
  "age": "abc"
}
```

Response:

```json
{
  "detail": [
    {
      "msg": "Input should be a valid integer"
    }
  ]
}
```

Status Code:

```http
422 Unprocessable Entity
```

This happens automatically.

---

# 2. HTTPException

Used when data format is valid, but business rules fail.

Example:

```python
from fastapi import HTTPException

@app.get("/users/{user_id}")
def get_user(user_id: int):

    if user_id != 1:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {"id": 1}
```

Response:

```json
{
  "detail": "User not found"
}
```

Status:

```http
404 Not Found
```

---

## Real Examples

### Login

```python
raise HTTPException(
    status_code=401,
    detail="Invalid username or password"
)
```

### Forbidden Resource

```python
raise HTTPException(
    status_code=403,
    detail="You cannot access this resource"
)
```

### Duplicate Email

```python
raise HTTPException(
    status_code=409,
    detail="Email already exists"
)
```

---

# 3. Try/Except

Used when something unexpected may fail.

Example:

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    return {"error": "Cannot divide by zero"}
```

FastAPI Example:

```python
try:
    user = db.get_user(id)
except Exception:
    raise HTTPException(
        status_code=500,
        detail="Internal Server Error"
    )
```

---

# Common Status Codes

| Code | Meaning          |
| ---- | ---------------- |
| 200  | Success          |
| 201  | Created          |
| 400  | Bad Request      |
| 401  | Unauthorized     |
| 403  | Forbidden        |
| 404  | Not Found        |
| 409  | Conflict         |
| 422  | Validation Error |
| 500  | Server Error     |

These are used daily in backend jobs.

---

# Custom Error Responses

Instead of generic messages:

```python
raise HTTPException(
    status_code=404,
    detail="User not found"
)
```

You can return structured errors:

```python
raise HTTPException(
    status_code=404,
    detail={
        "error_code": "USER_NOT_FOUND",
        "message": "User does not exist"
    }
)
```

Response:

```json
{
  "detail": {
    "error_code": "USER_NOT_FOUND",
    "message": "User does not exist"
  }
}
```

Large companies often use this style.

---

# Custom Exception Classes

For reusable errors:

```python
class UserNotFound(Exception):
    pass
```

Raise:

```python
raise UserNotFound()
```

Handle:

```python
from fastapi import Request
from fastapi.responses import JSONResponse

@app.exception_handler(UserNotFound)
async def handler(request: Request, exc: UserNotFound):
    return JSONResponse(
        status_code=404,
        content={"message": "User not found"}
    )
```

Useful in large projects.

---

# Database Errors

Very common in real APIs.

Example:

```python
try:
    db.commit()
except Exception:
    db.rollback()
    raise HTTPException(
        status_code=500,
        detail="Database error"
    )
```

Possible causes:

* Connection lost
* Duplicate key
* Constraint violation
* Database down

---

# Authentication Errors

Used in JWT login systems.

```python
raise HTTPException(
    status_code=401,
    detail="Token expired"
)
```

```python
raise HTTPException(
    status_code=401,
    detail="Invalid token"
)
```

---

# Logging Errors

Real systems don't just return errors.

They also log them.

```python
import logging

logger = logging.getLogger(__name__)

try:
    do_something()
except Exception as e:
    logger.error(str(e))
```

This helps developers debug production issues.

---

# Error Handling Roadmap for FastAPI

Learn in this order:

1. Pydantic Validation Errors
2. HTTPException
3. Status Codes
4. Try / Except
5. Custom Exceptions
6. Global Exception Handlers
7. Database Error Handling
8. Authentication Errors
9. Logging
10. Monitoring (advanced)

---

## Real Backend Flow

Imagine a registration API:

```text
POST /register
      │
      ▼
Pydantic checks JSON
      │
      ▼
Email already exists?
      │
      ├─ Yes → 409 Conflict
      │
      ▼
Save to Database
      │
      ├─ DB fails → 500
      │
      ▼
User Created
      │
      ▼
201 Created
```

If you understand **Pydantic Validation + HTTPException + Status Codes + Try/Except**, you'll already understand about 80% of the error handling used in typical FastAPI backend projects.
