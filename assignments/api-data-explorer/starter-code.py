import requests
from fastapi import FastAPI, HTTPException, Query

POSTS_URL = "https://jsonplaceholder.typicode.com/posts"
app = FastAPI(title="API Data Explorer")


def fetch_posts():
    """Fetch posts from JSONPlaceholder and return them as Python data."""
    # TODO: Send a GET request with a timeout, check the response, and parse JSON.
    raise NotImplementedError


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/posts")
def list_posts(
    search: str | None = None,
    user_id: int | None = Query(default=None, gt=0),
):
    # TODO: Fetch the posts, apply any requested filters, and return the result.
    # If the upstream service fails, raise HTTPException with an appropriate status.
    raise NotImplementedError
