These are the **core API fundamentals** that every FastAPI developer must understand.

---

# 1. What is an API?

API (**Application Programming Interface**) allows two applications to communicate.

### Real-world example

Imagine a restaurant:

```text
Customer → Waiter → Kitchen
```

* Customer = Client
* Waiter = API
* Kitchen = Server

The customer doesn't enter the kitchen directly. The waiter carries requests and responses.

Similarly:

```text
Android App → API → FastAPI Server
```

---

# 2. GET Request

**GET** is used to **retrieve data** from the server.

### Example

Request:

```http
GET /alerts
```

Meaning:

> "Server, give me all alerts."

Response:

```json
{
  "alerts": 15
}
```

### Real-world examples

```text
GET /users
GET /products
GET /alerts
GET /students
```

Use GET when you want to **read data**.

---

# 3. POST Request

**POST** is used to **send data to the server**.

### Example

Your Android app sends network traffic features:

Request:

```http
POST /predict
```

Body:

```json
{
  "duration": 100,
  "packets": 50
}
```

Server processes the data and returns:

```json
{
  "prediction": "Attack"
}
```

Use POST when you want to:

* Create new data
* Send data for processing
* Upload information

---

# 4. Request

A **request** is a message sent by the client to the server.

A request contains:

### URL

```text
/predict
```

### Method

```text
GET
POST
PUT
DELETE
```

### Data (optional)

```json
{
  "duration": 100
}
```

Example request:

```http
POST /predict HTTP/1.1
```

```json
{
  "duration": 100,
  "packets": 50
}
```

---

# 5. Response

A **response** is what the server sends back.

Example:

```json
{
  "prediction": "Benign"
}
```

Response usually contains:

### Data

```json
{
  "prediction": "Attack"
}
```

### Status Code

```http
200 OK
```

---

# 6. JSON

JSON (**JavaScript Object Notation**) is the standard format used to exchange data in APIs.

Example:

```json
{
  "name": "John",
  "age": 22
}
```

JSON stores data as:

```json
{
  "key": "value"
}
```

Examples:

```json
{
  "prediction": "Attack"
}
```

```json
{
  "temperature": 25
}
```

```json
{
  "student": "Alice"
}
```

---

# Complete Flow Example

Suppose your NIDS app wants a prediction.

### Step 1: Client sends Request

```http
POST /predict
```

```json
{
  "flow_duration": 120,
  "packet_count": 60
}
```

↓

### Step 2: FastAPI receives Request

```python
@app.post("/predict")
```

↓

### Step 3: ML Model Predicts

```python
prediction = model.predict(data)
```

↓

### Step 4: Server sends Response

```json
{
  "prediction": "Attack"
}
```

↓

### Step 5: Android App displays result

```text
Attack Detected
```

---

# Easy Exam Definition

| Term     | Definition                                          |
| -------- | --------------------------------------------------- |
| API      | A mechanism that allows applications to communicate |
| GET      | Retrieves data from the server                      |
| POST     | Sends data to the server                            |
| Request  | Message sent from client to server                  |
| Response | Message sent from server to client                  |
| JSON     | Lightweight format used to exchange data            |

### One-line summary

```text
Client sends a Request (GET/POST) containing JSON data to an API, and the server processes it and returns a Response in JSON format.
```


For FastAPI interviews, the next topics are usually **Path Parameters**, **Query Parameters**, **Request Body (Pydantic Models)**, and **Status Codes**. These are the concepts that come right after GET/POST basics.

A **query parameter** is extra information you attach to a URL to pass data to the backend (like FastAPI or Flask). It usually comes after a `?` in the URL and is written as `key=value`.  

### Example
```http
http://127.0.0.1:8000/items?skip=10&limit=5
```
Here:
- `skip=10` → query parameter named `skip` with value `10`
- `limit=5` → query parameter named `limit` with value `5`

---

### In FastAPI
You can read query parameters by defining them as function arguments:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
```

- If you visit `/items?skip=20&limit=5`, FastAPI will give:
  ```json
  {"skip": 20, "limit": 5}
  ```

---

### Difference from Path Parameters
- **Path parameter**: part of the URL itself  
  `/items/42` → `42` is a path parameter (item id).
- **Query parameter**: extra info after `?`  
  `/items?limit=10` → `limit` is a query parameter.

---

**Pydantic** is a Python library that FastAPI relies on for **data validation and settings management**. It uses Python type hints to automatically check, parse, and serialize data.  

### 🔑 What Pydantic Does
- **Validation**: Ensures incoming data matches the expected type.
- **Parsing**: Converts data into proper Python types (e.g., `"123"` → `int`).
- **Serialization**: Converts Python objects back into JSON for responses.
- **Error handling**: If data doesn’t match, it returns clear error messages.

---

### 📌 Example in FastAPI
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True

@app.post("/items/")
def create_item(item: Item):
    return item
```

- If you send JSON:
  ```json
  {"name": "Laptop", "price": 999.99}
  ```
  → FastAPI (via Pydantic) validates it, fills `in_stock=True`, and returns the object.

- If you send invalid data:
  ```json
  {"name": "Laptop", "price": "cheap"}
  ```
  → Pydantic raises a validation error because `"cheap"` is not a float.

---

### 🚀 Why It’s Important
- Makes FastAPI **safe and reliable** by catching bad input before it reaches your logic.
- Eliminates boilerplate code for manual validation.
- Integrates seamlessly with FastAPI’s auto-generated docs (`/docs`), showing request/response schemas.

---

👉 In short: **FastAPI builds on Pydantic to give you automatic validation and clean data handling.** That’s why FastAPI feels so modern compared to Flask — you don’t have to write manual checks.  

