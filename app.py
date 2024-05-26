from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []  # List to store the tasks

@app.route('/')  # Home route
def index():
    """
    Renders the index.html template and passes the tasks list to it.

    Returns:
        The rendered index.html template.
    """
    return render_template('index.html', tasks=tasks, enumerate=enumerate)

@app.route('/add', methods=['POST'])  # Add route
def add():
    """
    Adds a new task to the tasks list.

    Returns:
        Redirects to the index route.
    """
    task = request.form('task')
    if task:
        tasks.append(task)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')  # Delete route
def delete(task_id):
    """
    Deletes a task from the tasks list based on the given task_id.

    Args:
        task_id (int): The id of the task to be deleted.

    Returns:
        Redirects to the index route.
    """
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)