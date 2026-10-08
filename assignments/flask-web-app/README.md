# 📘 Assignment: Web App Development with Flask and HTML

## 🎯 Objective

Build a small Flask web app that displays a list of tasks and lets users add new ones through a simple HTML form. This assignment connects Python logic with web interfaces, teaching students how data moves between the browser and the server.

## 📝 Tasks

### 🛠️ Create a Flask App

#### Description
Set up a minimal Flask application that serves a homepage and renders a task list.

#### Requirements
Completed program should:

- Import Flask and create an app instance
- Define a route for the homepage such as `/`
- Render an HTML template named `index.html`
- Display a heading like "Student Task Board"
- Run the app locally with Flask's development server

### 🛠️ Build the User Interface

#### Description
Create a simple web page with a form for entering a task and a section that shows all current tasks.

#### Requirements
Completed program should:

- Use HTML to create a form with an input field and submit button
- Show a list of tasks from a Python data structure
- Include a visible status for each task, such as "Done" or "Not Done"
- Use CSS styling or simple HTML structure to keep the page readable and organized

### 🛠️ Handle User Input and Task Updates

#### Description
Add backend logic so users can submit new tasks and update task status.

#### Requirements
Completed program should:

- Accept form data in a `POST` request
- Add new tasks to an in-memory list
- Prevent empty task submissions
- Provide a way to mark a task as complete or delete it
- Redirect or refresh the page after the update so the user sees the new state

