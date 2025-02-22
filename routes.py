from main import app, db
from models import Task
from flask import render_template, redirect, url_for
from models import Task
from datetime import datetime

import forms

@app.route("/")
@app.route("/index")
def index():
    tasks = Task.query.all()
    return render_template("index.html", tasks=tasks)

@app.route("/add-task", methods=["GET", "POST"])
def add_task():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        new_task = Task(title=form.title.data, task_description=form.task_description.data, status=form.status.data, due_date=form.due_date.data, created_date=datetime.today().date())
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("add.html", form=form)

@app.route("/update-task/<int:id>", methods=["GET", "POST"])
def update_task(id):
    task = db.get_or_404(Task, id)
    task_update = forms.AddTaskForm(
        title=task.title,
        task_description=task.task_description,
        due_date=task.due_date,
        status=task.status
    )
    if task_update.validate_on_submit():
        task.title=task_update.title.data
        task.task_description=task_update.task_description.data
        task.due_date=task_update.due_date.data
        task.status=task_update.status.data
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("edit.html", form=task_update, is_edit=True)

@app.route("/delete-task/<int:id>")
def delete_task(id):
    task = db.get_or_404(Task, id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for("index"))