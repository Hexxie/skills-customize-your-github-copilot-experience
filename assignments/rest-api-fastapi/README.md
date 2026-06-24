# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to design and implement a simple REST API using the FastAPI framework. Build endpoints, validate input with Pydantic models, and run the service with Uvicorn.

## 📝 Tasks

### 🛠️ Task 1 — Core API

#### Description
Create a small REST API that exposes CRUD-style endpoints for a simple resource (e.g., `Item`). Use FastAPI and Pydantic for request/response validation.

#### Requirements

Completed project should:

- Implement at least the following endpoints: `GET /`, `GET /items/{id}`, and `POST /items/`.
- Use Pydantic models for request validation and response serialization.
- Return appropriate HTTP status codes for success and error cases.
- Keep data in memory (a simple dict) for the purpose of the assignment.

### 🛠️ Task 2 — Enhancements (optional)

#### Description
Add one or more enhancements to showcase additional REST concepts.

#### Examples

- Add `PUT` and `DELETE` endpoints
- Add pagination or query filtering for `GET /items/`
- Persist data to a CSV file or simple SQLite DB
- Add API documentation examples and tests

## 📂 Starter files

- `starter-code.py` — minimal FastAPI app skeleton to get started
- `requirements.txt` — dependencies to install (`fastapi`, `uvicorn`)

## ▶️ How to run

Install dependencies and run with Uvicorn:

```bash
pip3 install -r requirements.txt
uvicorn starter-code:app --reload --port 8000
```

Open the interactive docs at `http://127.0.0.1:8000/docs`.

## ✅ Submission

1. Ensure your API runs without errors.
2. Add inline comments explaining key functions and decisions.
3. Submit `starter-code.py` and any additional files you added.

## 📚 Skills practiced

- Designing REST endpoints
- Input validation with Pydantic
- Running ASGI apps with Uvicorn
- Handling HTTP status codes and simple persistence

Good luck — build something useful and well-documented!
