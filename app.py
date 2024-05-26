from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)

@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks, enumerate=enumerate)

@app.route('/add', methods=['POST'])
def add():
    task_content = request.form.get('task')
    if task_content:
        new_task = Task(task=task_content)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    task_to_delete = Task.query.get_or_404(task_id)
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['POST'])
def edit(task_id):
    task_content = request.form.get('task')
    task_to_edit = Task.query.get_or_404(task_id)
    if task_content:
        task_to_edit.task = task_content
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete(task_id):
    task_to_complete = Task.query.get_or_404(task_id)
    task_to_complete.completed = True
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/incomplete/<int:task_id>')
def incomplete(task_id):
    task_to_incomplete = Task.query.get_or_404(task_id)
    task_to_incomplete.completed = False
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/completed')
def completed():
    tasks = Task.query.filter_by(completed=True).all()
    return render_template('index.html', tasks=tasks, enumerate=enumerate)

@app.route('/incomplete')
def incomplete_tasks():
    tasks = Task.query.filter_by(completed=False).all()
    return render_template('index.html', tasks=tasks, enumerate=enumerate)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
