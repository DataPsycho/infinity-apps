from flask import Flask, render_template, request
from flask import redirect, url_for, jsonify, abort
from sqlalchemy import Column, Integer, String, Boolean
from flask_sqlalchemy import SQLAlchemy
import sys
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://datapsycho:datapsycho@localhost:5432/ishkul'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)

migrate = Migrate(app, db)

class Todo(db.Model):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True)
    description = Column(String(), nullable=False)
    completed = Column(Boolean, nullable=False, default=False)
    # referance from parents
    list_id = Column(Integer, db.ForeignKey('todolists.id'), nullable=False)

    def __repr__(self):
        return f'<Todo {self.id} {self.description} >'

class TodoList(db.Model):
    __tablename__ = 'todolists'
    id = Column(Integer, primary_key=True)
    name = Column(String(), nullable=False)
    # referance of child
    todos = db.relationship('Todo', backref='list', lazy=True)

    def __repr__(self):
        return f'<Todo {self.id} {self.name} >'

# removed after migration
# db.create_all()

@app.route('/todos/<todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    try:
        Todo.query.filter_by(id=todo_id).delete()
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
    return jsonify({'success': True})

@app.route('/todos/create', methods=['POST',])
def create_todo():
    error = False
    body = {}
    try:
        description = request.get_json()['description']
        todo = Todo(description=description)
        db.session.add(todo)
        db.session.commit()
        body['description'] = todo.description
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        abort(400)
    else:
        return jsonify(body)


@app.route('/todos/<todos_id>/set-completed', methods=['POST'])
def set_completed_todo(todos_id):
    try:
        completed = request.get_json()['completed']
        todo = Todo.query.get(todos_id)
        todo.completed = completed
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
    finally:
        db.session.close()
    return redirect(url_for('index'))


@app.route('/lists/<list_id>')
def get_list_todos(list_id):
    return render_template(
        'index.html',
        lists = TodoList.query.all(),
        active_list = TodoList.query.get(list_id),
        todos = Todo.query.filter_by(list_id=list_id).order_by('id').all()
    )

@app.route('/')
def index():
    return redirect(url_for('get_list_todos', list_id=1))
