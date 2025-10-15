from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    status = db.Column(db.Boolean)

@app.route('/')
def index():
    all_tasks = Task.query.all()   
    print(all_tasks) 
    return render_template('base.html', all_tasks=all_tasks)

@app.route('/add', methods=["POST"])
def add():
    task_title = request.form.get("task_title")
    new_task = Task(title=task_title, status=False) # type:ignore
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)