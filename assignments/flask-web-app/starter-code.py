from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Review Python basics", "done": False},
    {"id": 2, "title": "Plan project ideas", "done": True},
]


@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)


@app.post("/tasks")
def add_task():
    title = request.form.get("title", "").strip()
    if not title:
        return redirect(url_for("index"))

    # TODO: Add the new task to the tasks list.
    return redirect(url_for("index"))


# TODO: Add a route to mark a task complete or delete it.


if __name__ == "__main__":
    app.run(debug=True)
