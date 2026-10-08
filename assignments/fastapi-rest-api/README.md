# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API using FastAPI to manage tasks. This assignment introduces students to API design, request handling, data validation, and basic CRUD operations in a modern Python web framework.

## 📝 Tasks

### 🛠️ Create a FastAPI Application

#### Description
Set up a FastAPI app and create an endpoint that confirms the API is running.

#### Requirements
Completed program should:

- Create a FastAPI application instance
- Define a basic health-check route such as `GET /health`
- Return a JSON response like `{"status": "ok"}`
- Run the app locally with Uvicorn


### 🛠️ Build a Task Resource and CRUD Endpoints

#### Description
Create a simple API for managing tasks, including creating, reading, updating, and deleting items.

#### Requirements
Completed program should:

- Define a `Task` model with fields such as `id`, `title`, `description`, and `completed`
- Create an endpoint to add a new task with `POST /tasks`
- Create an endpoint to list all tasks with `GET /tasks`
- Create an endpoint to retrieve one task by ID with `GET /tasks/{task_id}`
- Create an endpoint to update a task with `PUT /tasks/{task_id}`
- Create an endpoint to delete a task with `DELETE /tasks/{task_id}`
- Return JSON responses using FastAPI's automatic response handling


### 🛠️ Add Validation and Error Handling

#### Description
Improve the API by validating input and handling invalid requests gracefully.

#### Requirements
Completed program should:

- Use Pydantic models to validate request data
- Reject invalid task values such as missing required fields
- Return clear error responses for missing or invalid task IDs
- Demonstrate a working API flow using a few sample requests
