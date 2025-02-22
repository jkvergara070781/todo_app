from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired

class AddTaskForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    task_description = TextAreaField("Description", validators=[DataRequired()])
    choices = [("In-progress", "In-progress"), ("Completed", "Completed")]
    status = SelectField("Select status", choices=choices)
    due_date = DateField("Due", validators=[DataRequired()])
    submit = SubmitField("Submit")