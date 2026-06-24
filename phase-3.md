Yes. In FastAPI, **Path Parameters** and **Query Parameters** are how you pass data to an endpoint.

## 1. Path Parameters

A path parameter is part of the URL path.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}
```

Request:

```
GET /items/10
```

Response:

```json
{
  "item_id": 10
}
```

Here `10` is passed as `item_id`.

---

## 2. Query Parameters

A query parameter comes after `?` in the URL.

```python
@app.get("/products")
def get_products(limit: int):
    return {"limit": limit}
```

Request:

```
GET /products?limit=5
```

Response:

```json
{
  "limit": 5
}
```

Here FastAPI reads `limit=5`.

---

## 3. Default Query Parameters

You can give a default value.

```python
@app.get("/products")
def get_products(limit: int = 10):
    return {"limit": limit}
```

If user does:

```
GET /products
```

Response:

```json
{
  "limit": 10
}
```

Because no limit was provided, FastAPI uses the default value `10`.

---

## Real Example: 100 Products in Database

Imagine you have 100 products.

```python
products = ["P1", "P2", "P3", ..., "P100"]

@app.get("/products")
def get_products(limit: int = 10):
    return products[:limit]
```

### Request 1

```
GET /products
```

Response:

```json
["P1","P2","P3","P4","P5","P6","P7","P8","P9","P10"]
```

Only first 10 products because default limit is 10.

---

### Request 2

```
GET /products?limit=20
```

Response:

```json
["P1","P2", ... ,"P20"]
```

Returns first 20 products.

---

## 4. Optional Query Parameters

Sometimes a parameter is optional.

```python
from typing import Optional

@app.get("/search")
def search(name: Optional[str] = None):
    return {"name": name}
```

Request:

```
GET /search
```

Response:

```json
{
  "name": null
}
```

Request:

```
GET /search?name=laptop
```

Response:

```json
{
  "name": "laptop"
}
```

---

## Path + Query Together

```python
@app.get("/users/{user_id}")
def get_user(user_id: int, limit: int = 10):
    return {
        "user_id": user_id,
        "limit": limit
    }
```

Request:

```
GET /users/5?limit=20
```

Response:

```json
{
  "user_id": 5,
  "limit": 20
}
```

* `5` → Path Parameter (`user_id`)
* `20` → Query Parameter (`limit`)

### Quick Memory Trick

| Type            | Example URL        | Purpose                         |
| --------------- | ------------------ | ------------------------------- |
| Path Parameter  | `/users/5`         | Identify a specific resource    |
| Query Parameter | `/users?limit=10`  | Filter, search, paginate        |
| Optional Query  | `/users?name=john` | Extra filtering                 |
| Default Query   | `limit=10`         | Used when user provides nothing |

So your understanding is correct: **if there are 100 records and `limit=10` is the default, then `GET /products` will return only the first 10 records unless the client specifies another limit.**
