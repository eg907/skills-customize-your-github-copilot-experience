# 📘 Assignment: API Data Explorer

## 🎯 Objective

Build a small FastAPI app that retrieves JSON data from a public API and lets users explore it through search and filter endpoints. Practice making HTTP requests, working with JSON, and designing useful API routes.

## 📝 Tasks

### 🛠️ Retrieve and Explore Public API Data

#### Description
Connect your Python app to JSONPlaceholder's posts endpoint and inspect the JSON data returned by the service.

#### Requirements
Completed program should:

- Request data from `https://jsonplaceholder.typicode.com/posts`
- Parse the response as JSON and handle unsuccessful HTTP responses
- Display the number of posts and the title of at least one post
- Use a timeout for the HTTP request


### 🛠️ Create Search and Filter Endpoints

#### Description
Expose the retrieved posts through a FastAPI app so users can list posts, search by title, or filter by user ID.

#### Requirements
Completed program should:

- Create a FastAPI application with a `GET /posts` endpoint that returns posts as JSON
- Support an optional `search` query parameter that matches post titles without regard to letter case
- Support an optional `user_id` query parameter that filters posts by user ID
- Return an empty list when no posts match the requested search or filter
- Include a `GET /health` endpoint that returns `{"status": "ok"}`


### 🛠️ Validate Inputs and Try the API

#### Description
Add clear behavior for invalid requests and try the endpoints using the interactive API documentation.

#### Requirements
Completed program should:

- Validate that `user_id` is a positive integer
- Return an appropriate HTTP error if the upstream data service cannot be reached
- Run the app locally with Uvicorn
- Demonstrate requests to `/posts`, `/posts?search=qui`, and `/posts?user_id=1` using `/docs`
