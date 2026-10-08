from fastapi import FastAPI

app = FastAPI(title="Task API")

# In-memory task storage
items = []


@app.get("/health")
def health_check():
    return {"status": "ok"}


# TODO: Add task model, endpoints, validation, and CRUD logic
