from flask import render_template, flash, redirect, session, url_for, request, g
from flask_admin.contrib.sqla import ModelView
from app import app, db, admin
from .models import User
from .forms import LoginForm

err = None

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title="Sign In", form=form)


























'''
#Homepage:View all tasks
@app.route('/', methods=['GET'])
def getAllTasks():
    tasks = User.query.all()
    return render_template('index.html',
                               title='homepage',
                               tasks=tasks
    )

#view finished task
@app.route("/finished", methods=['GET'])
def getFinishedTask():
    tasks = User.query.filter(User.status == "finished")
    return render_template('task_list.html',
                           title=' Finished Tasks',
                           tasks=tasks
    )

#Order all tasks by due date
@app.route("/view_task", methods=['GET'])
def taskOrderByDate():
    tasks = User.query.order_by(User.username)
    return render_template('task_list.html',
                           title='All Tasks',
                           tasks=tasks
    )

#Create Task
@app.route('/create_task', methods=['GET','POST'])
def create_task():
    global err
    form = LoginForm()
    flash('Errors="%s"' %
          (form.errors))
    if form.validate_on_submit():
        t = User( title=form.title.data, status=form.status.data, description = form.description.data, type=form.type.data, date=form.date.data)
        if t:
            db.session.add(t)
            try:
                db.session.commit()
            except Exception as e:
                err = e
                raise e
            return redirect('/view_task')
    return render_template('create_task.html',
                           title='Create Task',
                           form=form)

#view unfinished tasks
@app.route('/unfinished', methods=['GET'])
def getUnfinished():
    tasks = User.query.filter(User.status == 'unfinished')
    return render_template('task_list.html',
                           title='Unfinished Task',
                           tasks=tasks)

# view tasks that typed "eat
@app.route('/eat', methods=['GET'])
def getEat():
    tasks = User.query.filter(User.type == 'eat')
    return render_template('task_list.html',
                           title='Task-Eat',
                           tasks=tasks)

# view tasks that typed "life"
@app.route('/life', methods=['GET'])
def getLife():
    tasks = User.query.filter(User.type == 'life')
    return render_template('task_list.html',
                           title='Task-Life',
                           tasks=tasks)

# view tasks that typed "study"
@app.route('/study', methods=['GET'])
def getStudy():
    tasks = User.query.filter(User.type == 'study')
    return render_template('task_list.html',
                           title='Task-Study',
                           tasks=tasks)

#delete a task
@app.route('/delete_task/<id>', methods=['GET'])
def delete_task(id):
    task = User.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return redirect('/view_task')

#edit a task
@app.route('/edit_task/<id>', methods=['GET','POST'])
def edit_task(id):
    user = User.query.get(id)
    form = LoginForm(obj=user)
    flash('Errors="%s"' %
          (form.errors))
    if form.validate_on_submit():
        t = user
        t.status = form.status.data
        t.title = form.title.data
        t.type = form.type.data
        t.date = form.date.data
        t.description = form.description.data
        db.session.commit()
        return redirect('/view_task')
    return render_template('create_task.html',
                           title='Edit Task',
                           form=form)
'''
