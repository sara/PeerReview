from flask import request, render_template, redirect, url_for
from app import app
from forms import SearchForm
from sqlalchemy import inspect
from models import session
from collections import namedtuple

@app.route('/', methods=['GET', 'POST'])
def landing():
  form = SearchForm(request.form)
  if request.method == 'POST' and form.validate():
    if form.data['studentid']:
      return redirect(url_for('get_results', category='students', name=form.data['studentid']))
    elif form.data['professorid']:
      return redirect(url_for('get_results', category='prof', name=form.data['professorid']))
  else:
    return render_template('land.html', form=form)

@app.route('/results/<name>', methods=['GET', 'POST'])
def get_students(name):
  result = session.execute("select * from students where name=:val",{'val': name})
  Student = namedtuple('Student', result.keys()) 
  students = [Student(*r) for r in result.fetchall()]
  students = [student.__dict__ for student in students]
  if len(students) != 0:
    return render_template('results.html', students=students)
  return redirect (url_for('land'))
  

#select from taken, get only unique classes (i.e. ignore reviewers)
def get_profs(name):
  result = session.execute("select * from students where name=:val",{'val': name})
  Student = namedtuple('Student', result.keys()) 
  students = [Student(*r) for r in result.fetchall()]
  students = [student.__dict__ for student in students]
  if len(students) != 0:
    return render_template('results.html', students=students)
  return redirect (url_for('land'))
 

@app.route('/create', methods=['GET', 'POST'])
def land():
  return render_template('create.html')
