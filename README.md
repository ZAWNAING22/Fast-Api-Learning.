## Project Goal
Build a complete FastAPI application while learning backend fundamentals, API development, data validation, error handling, machine learning model deployment, and batch prediction workflows.

# FastAPI Learning Journey: From Fundamentals to Machine Learning APIs

## Overview

This repository documents my hands-on learning of FastAPI by building and testing REST APIs, validating data with Pydantic, handling errors, integrating machine learning models, and creating file upload endpoints for batch predictions.

The project follows a practical approach, starting from backend fundamentals and progressing toward a complete Machine Learning Prediction API.

---

## Learning Roadmap

### 1. Core Backend Concepts

Before writing APIs, it is important to understand the fundamental concepts behind web applications.

Topics covered:

* Client–Server Architecture
* HTTP Protocol
* Requests and Responses
* JSON Data Format
* Introduction to Machine Learning Models

#### Key Takeaways

* How clients communicate with servers
* How APIs exchange data
* The role of HTTP methods and status codes
* Why JSON is the standard format for modern APIs
* How machine learning models can be exposed through APIs

---

### 2. Introduction to FastAPI

FastAPI is a modern Python framework for building high-performance APIs.

Topics covered:

* FastAPI installation
* Virtual environments
* Creating the first API endpoint
* Running applications with Uvicorn
* Interactive API documentation

#### Key Takeaways

* Building APIs quickly with minimal code
* Running development servers using Uvicorn
* Testing endpoints using Swagger UI and ReDoc

---

### 3. API Fundamentals

Learned the essential building blocks of REST APIs.

Topics covered:

* GET requests
* POST requests
* Request handling
* Response generation
* JSON serialization

#### Key Takeaways

* Retrieving data using GET endpoints
* Sending data using POST endpoints
* Understanding request-response cycles
* Working with JSON payloads

---

### 4. Path and Query Parameters

Explored how APIs receive user input through URLs.

Topics covered:

* Path Parameters
* Query Parameters
* Optional Parameters
* Parameter Validation

#### Key Takeaways

* Creating dynamic routes
* Filtering and searching data
* Handling optional user inputs
* Applying validation rules

---

### 5. Request Body and Data Validation

Learned how to process structured input data using Pydantic models.

Topics covered:

* Pydantic Models
* Request Bodies
* Input Validation
* Type Enforcement

#### Key Takeaways

* Defining data schemas
* Automatic validation of incoming requests
* Reducing runtime errors
* Improving API reliability and maintainability

---

### 6. Error Handling

Implemented proper error handling strategies to make APIs robust.

Topics covered:

* Validation Errors
* Missing Fields
* HTTP Exceptions
* Custom Error Responses

#### Key Takeaways

* Returning meaningful error messages
* Using appropriate HTTP status codes
* Handling invalid user input gracefully
* Creating custom exceptions for business logic

---

### 7. Machine Learning API Project

Built a House Price Prediction API using a trained Scikit-Learn model.

Topics covered:

* Model Training
* Regression Concepts
* Classification Concepts
* Model Serialization
* Loading Models at Startup

Tools used:

* Scikit-Learn
* Pickle
* Joblib
* FastAPI

#### Key Takeaways

* Saving trained models
* Loading models efficiently
* Serving predictions through REST APIs
* Connecting machine learning with backend development

---

### 8. File Upload API for Batch Predictions

Extended the API to support bulk predictions from uploaded CSV files.

Topics covered:

* File Upload Handling
* CSV Processing
* Batch Inference
* Result Generation

#### Key Takeaways

* Receiving files through API endpoints
* Processing datasets in bulk
* Running predictions on multiple records
* Returning prediction results efficiently

---

## Technologies Used

* Python
* FastAPI
* Uvicorn
* Pydantic
* Scikit-Learn
* Pickle
* Joblib
* Pandas
* CSV Processing

---

## Skills Demonstrated

* REST API Development
* Backend Fundamentals
* Data Validation
* Error Handling
* Machine Learning Deployment
* File Processing
* API Documentation
* Production-Oriented API Design

---

## Outcome

By completing this project, I gained practical experience in building modern APIs with FastAPI, validating and processing user input, handling errors professionally, deploying machine learning models, and creating scalable endpoints for real-world prediction workflows.
