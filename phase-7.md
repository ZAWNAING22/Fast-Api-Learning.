This chapter is very important for **AI/ML APIs** because companies rarely send one row at a time. They often upload a CSV with thousands of records and expect predictions for all of them.

Using your **California House Price model**, let's see how it works in real life.

# Problem

You trained a model:

```python
model.predict(...)
```

Single prediction API:

```json
{
  "MedInc": 8.3,
  "HouseAge": 20,
  "AveRooms": 6.5
}
```

returns

```json
{
  "predicted_price": 350000
}
```

Good for one house.

But what if a real estate company has:

```csv
house1
house2
house3
...
house10000
```

Typing JSON 10,000 times is impossible.

Instead they upload:

```csv
MedInc,HouseAge,AveRooms
8.3,20,6.5
5.1,15,4.2
...
```

Your API:

1. Receives CSV
2. Reads CSV
3. Runs model on all rows
4. Returns predictions

---

# File Upload API

FastAPI provides:

```python
from fastapi import UploadFile, File
```

Example:

```python
@app.post("/predict-batch")
async def predict_batch(
    file: UploadFile = File(...)
):
    pass
```

When user uploads:

```csv
houses.csv
```

FastAPI puts it inside:

```python
file
```

---

# What is File(...)?

```python
file: UploadFile = File(...)
```

`File(...)` tells FastAPI:

> Expect a file from the request.

Without it:

```python
file: UploadFile
```

FastAPI doesn't know it comes from multipart/form-data upload.

Think of it like:

```python
name: str = Query(...)
```

for query parameters.

and

```python
user: User
```

for JSON body.

and

```python
file: UploadFile = File(...)
```

for uploaded files.

---

# What is UploadFile?

FastAPI has two options:

### Option 1

```python
file: bytes = File(...)
```

Loads whole file into memory.

Good for:

* small images
* small txt files

Bad for:

* 500MB CSV

---

### Option 2

```python
file: UploadFile = File(...)
```

Creates a file-like object.

Better for:

* CSV
* PDFs
* Images
* Videos

Real projects almost always use:

```python
UploadFile
```

because it is memory efficient.

---

# UploadFile Properties

### filename

```python
file.filename
```

Example:

```python
houses.csv
```

---

### content_type

```python
file.content_type
```

Example:

```python
text/csv
```

Useful validation:

```python
if file.content_type != "text/csv":
    raise HTTPException(
        status_code=400,
        detail="Upload CSV only"
    )
```

---

# Reading Uploaded CSV

## Method 1

```python
content = await file.read()
```

Returns bytes.

Example:

```python
b'MedInc,HouseAge\n8.3,20'
```

Convert:

```python
content.decode("utf-8")
```

---

# io Library

Python's built-in:

```python
import io
```

Very common in ML APIs.

Why?

Because:

```python
pandas.read_csv()
```

expects a file-like object.

But uploaded data is often just text in memory.

So we create a virtual file.

---

# StringIO

```python
import io

csv_string = """
MedInc,HouseAge
8.3,20
"""

buffer = io.StringIO(csv_string)
```

Now:

```python
pd.read_csv(buffer)
```

works.

Think:

```text
Real file on disk
     ↓
Virtual file in memory
```

---

# Complete Example

```python
import io
import pandas as pd

content = await file.read()

df = pd.read_csv(
    io.StringIO(
        content.decode("utf-8")
    )
)
```

Now:

```python
print(df.head())
```

Output:

```text
   MedInc  HouseAge
0    8.3        20
1    5.1        15
```

---

# Running Predictions

```python
preds = model.predict(df)
```

Output:

```python
[320000, 250000, 400000]
```

Add to dataframe:

```python
df["prediction"] = preds
```

Result:

```text
MedInc HouseAge prediction
8.3    20      320000
5.1    15      250000
```

---

# Returning JSON

Small datasets:

```python
return df.to_dict(
    orient="records"
)
```

Output:

```json
[
  {
    "MedInc":8.3,
    "prediction":320000
  }
]
```

Good for:

* 10 rows
* 50 rows

Bad for:

* 100,000 rows

---

# Why StreamingResponse?

Imagine:

```csv
500000 rows
```

Predictions:

```csv
500000 rows + prediction
```

Returning huge JSON:

```python
return df.to_dict(...)
```

consumes lots of RAM.

Instead generate CSV and stream it.

```python
from fastapi.responses import StreamingResponse
```

---

# StreamingResponse Concept

Normal response:

```text
Create entire file
↓
Store in memory
↓
Send
```

Streaming:

```text
Create small chunk
↓
Send
↓
Create next chunk
↓
Send
```

Like YouTube:

You don't download entire movie first.

You stream it.

Same idea.

---

# Batch Prediction Download

```python
import io

output = io.StringIO()

df.to_csv(
    output,
    index=False
)

output.seek(0)
```

Return:

```python
return StreamingResponse(
    output,
    media_type="text/csv",
    headers={
        "Content-Disposition":
        "attachment; filename=predictions.csv"
    }
)
```

Browser downloads:

```text
predictions.csv
```

---

# Real Company Workflow

### Real Estate Company

Uploads:

```text
houses.csv
```

Your API:

```text
Receive CSV
↓
Validate columns
↓
Load model
↓
Predict
↓
Add prediction column
↓
Return predictions.csv
```

---

### Bank Loan System

Uploads:

```text
loan_applications.csv
```

Returns:

```text
approved_probability.csv
```

---

### Cybersecurity Project

Uploads:

```text
network_flows.csv
```

Returns:

```text
attack_predictions.csv
```

Very relevant to your NIDS project.

---

# What You Should Know for Interviews

Understand these:

```python
from fastapi import UploadFile, File
from fastapi.responses import StreamingResponse
import io
```

And why:

| Component         | Purpose                          |
| ----------------- | -------------------------------- |
| File              | Accept uploaded file             |
| UploadFile        | Memory-efficient uploaded file   |
| await file.read() | Read contents                    |
| io.StringIO       | Convert text to file-like object |
| pandas.read_csv() | Load CSV                         |
| model.predict()   | Run predictions                  |
| StreamingResponse | Return large CSV efficiently     |

For your California Housing project, the complete production flow is:

```text
Client Upload CSV
        ↓
UploadFile
        ↓
io.StringIO
        ↓
pandas DataFrame
        ↓
model.predict()
        ↓
prediction column
        ↓
StreamingResponse
        ↓
predictions.csv download
```

That is almost exactly how many real-world batch prediction APIs are built.
