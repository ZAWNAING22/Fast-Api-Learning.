This chapter is teaching the **basic concepts you need before building a FastAPI application**, especially one that serves an ML model (like your NIDS project).

---

# 1. What is a Server?

A **server** is a computer program that waits for requests and sends back responses.

### Example

You open YouTube.

* Your phone sends a request.
* YouTube's server receives it.
* The server sends back videos and data.

**FastAPI** will act as your server.

```
Client ---> Server
        Request
Client <--- Server
        Response
```

---

# 2. What is a Client?

A **client** is anything that sends requests to a server.

Examples:

* Android app
* Web browser
* Postman
* Another program

In your NIDS project:

* Android app = Client
* FastAPI application = Server

---

# 3. What is HTTP?

**HTTP (HyperText Transfer Protocol)** is the language clients and servers use to communicate.

Without HTTP:

* Browser cannot talk to server
* Mobile app cannot talk to FastAPI

### Example

```
GET /alerts
```

means:

> "Server, please give me the alerts."

---

# 4. Request and Response

Communication happens in two steps.

### Request

Client asks for something.

Example:

```json
{
  "flow_id": 123
}
```

### Response

Server returns data.

```json
{
  "prediction": "Attack"
}
```

Flow:

```
Client
   |
Request
   ↓
Server
   |
Response
   ↓
Client
```

---

# 5. What is a URL?

A **URL** is the address of a resource on a server.

Example:

```text
http://127.0.0.1:8000/predict
```

Parts:

| Part      | Meaning        |
| --------- | -------------- |
| http      | Protocol       |
| 127.0.0.1 | Server address |
| 8000      | Port           |
| /predict  | Endpoint       |

---

# 6. What is an API?

API = **Application Programming Interface**

An API is a set of rules that lets programs communicate.

### Example

Your Android app sends:

```json
{
  "duration": 10,
  "packets": 200
}
```

FastAPI processes it and returns:

```json
{
  "prediction": "Benign"
}
```

That communication is an API call.

---

# 7. What is JSON?

JSON = **JavaScript Object Notation**

It is the most common data format used in APIs.

Example:

```json
{
  "name": "Attack",
  "confidence": 0.95
}
```

Why use JSON?

* Lightweight
* Easy to read
* FastAPI supports it naturally

---

# 8. HTTP Methods

Methods tell the server what action to perform.

### GET

Retrieve data.

```http
GET /alerts
```

Get all alerts.

---

### POST

Send data.

```http
POST /predict
```

Send network flow data for prediction.

---

### PUT

Update existing data.

```http
PUT /alert/1
```

Update alert information.

---

### DELETE

Remove data.

```http
DELETE /alert/1
```

Delete alert.

---

# 9. Status Codes

The server returns status codes to indicate what happened.

### 200 OK

Success.

```http
200 OK
```

---

### 201 Created

New resource created.

```http
201 Created
```

---

### 400 Bad Request

Client sent invalid data.

```http
400 Bad Request
```

---

### 404 Not Found

Resource doesn't exist.

```http
404 Not Found
```

---

### 500 Internal Server Error

Something failed on server.

```http
500 Internal Server Error
```

---

# 10. Project Structure

A clean FastAPI project might look like:

```text
project/
│
├── main.py
├── routes/
│   └── prediction.py
│
├── models/
│   └── model.pkl
│
├── services/
│   └── predictor.py
│
└── requirements.txt
```

Benefits:

* Easy to maintain
* Easy to scale
* Professional structure

---

# 11. ML Model Flow

This is the most important part for your NIDS project.

### Step 1

Network traffic is captured.

### Step 2

Traffic is converted into features.

Example:

```text
Flow Duration
Packet Count
Bytes/sec
```

### Step 3

Features are sent to FastAPI.

```json
{
  "flow_duration": 120,
  "packets": 50
}
```

### Step 4

FastAPI loads the trained model.

```python
model.predict(data)
```

### Step 5

Model predicts.

```text
Attack
```

or

```text
Benign
```

### Step 6

FastAPI returns result.

```json
{
  "prediction": "Attack"
}
```

---

# How Everything Fits Together (Your NIDS Project)

```text
Android App (Client)
        |
        | HTTP Request (JSON)
        v
FastAPI Server
        |
        | Sends Features
        v
ML Model (.pkl)
        |
        | Prediction
        v
FastAPI
        |
        | JSON Response
        v
Android App
```

### One-line exam answer

**A client sends an HTTP request containing JSON data to a FastAPI server. The server processes the request, passes the data to the ML model, receives the prediction, and returns the result as a JSON response with an appropriate HTTP status code.**
