# FastAPI

**FastAPI** is a modern Python framework used to build APIs quickly.

Think of it as:

```text
Android App / Website
          |
          v
       FastAPI
          |
          v
     ML Model / Database
```

In your NIDS project:

* Android app sends network flow data
* FastAPI receives it
* ML model predicts Attack/Benign
* FastAPI returns the result

---

# What is Uvicorn?

**Uvicorn** is the server that runs FastAPI.

Analogy:

* FastAPI = Restaurant kitchen
* Uvicorn = Waiter bringing orders to the kitchen

Without Uvicorn, FastAPI cannot receive requests.

Run command:

```bash
uvicorn main:app --reload
```

Meaning:

```text
main     -> main.py
app      -> FastAPI object
--reload -> auto restart when code changes
```

---

# Installation

### 1. Create Project Folder

```bash
mkdir fastapi_project
cd fastapi_project
```

---

### 2. Create Virtual Environment

Windows:

```bash
python -m venv venv
```

This creates:

```text
fastapi_project/
└── venv/
```

Virtual environment keeps project packages isolated.

---

### 3. Activate Virtual Environment

Windows CMD:

```cmd
venv\Scripts\activate
```

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Linux/Mac:

```bash
source venv/bin/activate
```

After activation:

```text
(venv) C:\project>
```

---

### 4. Install FastAPI and Uvicorn

```bash
pip install fastapi uvicorn
```

Check:

```bash
pip list
```

---

# First FastAPI App

Create:

```text
main.py
```

Code:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello FastAPI"}
```

---

# Create an Endpoint

Endpoint = URL path users can access.

Example:

```python
@app.get("/hello")
def hello():
    return {"message": "Welcome"}
```

Access:

```text
http://127.0.0.1:8000/hello
```

Response:

```json
{
  "message": "Welcome"
}
```

---

# Multiple Endpoints

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Home"}

@app.get("/about")
def about():
    return {"message": "About API"}

@app.get("/predict")
def predict():
    return {"prediction": "Benign"}
```

---

# Run FastAPI

```bash
uvicorn main:app --reload
```

Output:

```text
INFO: Uvicorn running on
http://127.0.0.1:8000
```

Open browser:

```text
http://127.0.0.1:8000
```

---

# Automatic API Documentation

One of FastAPI's best features.

You get documentation automatically.

---

## Swagger Docs

Open:

```text
http://127.0.0.1:8000/docs
```

Interface allows:

* View endpoints
* Send requests
* Test APIs
* See responses


---

## ReDoc

Open:

```text
http://127.0.0.1:8000/redoc
```

Cleaner documentation view.

Good for reading API specifications.


---

# Example with POST Request

```python
from fastapi import FastAPI

app = FastAPI()

@app.post("/predict")
def predict(data: dict):
    return {
        "received": data,
        "prediction": "Attack"
    }
```

Test in:

```text
http://127.0.0.1:8000/docs
```

Click:

```text
POST /predict
Try it out
Execute
```

---

# Complete Flow

```text
1. Create venv
       |
2. Activate venv
       |
3. pip install fastapi uvicorn
       |
4. Create main.py
       |
5. uvicorn main:app --reload
       |
6. Open browser
       |
7. /docs or /redoc
       |
8. Test endpoints
```

### Interview / Exam Answer

**FastAPI is a high-performance Python framework for building APIs. Uvicorn is an ASGI server used to run FastAPI applications. After creating and activating a virtual environment, FastAPI and Uvicorn can be installed using pip. Endpoints are created using decorators such as `@app.get()` and `@app.post()`. FastAPI automatically generates interactive API documentation at `/docs` (Swagger UI) and `/redoc` (ReDoc).**
