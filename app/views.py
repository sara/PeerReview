from flask import request, render_template, redirect, url_for
from app import app
from forms import SearchForm
from sqlalchemy import inspect
from models import session
from collections import namedtuple
from urllib import quote


@app.route('/', methods=['GET', 'POST'])
def landing():
  form = SearchForm(request.form)
  if request.method == 'POST' and form.validate():
    if form.data['studentid']:
      return redirect(url_for('get_students', name=form.data['studentid']))
    elif form.data['professorid']:
      return redirect(url_for('get_profs', name=form.data['professorid']))
  else:
    return render_template('land.html', form=form)


@app.route('/students/<name>', methods=['GET', 'POST'])
def get_students(name):
  #if request.method == 'POST':
   # return redirect(url_for('get_profile'))

  result = session.execute("select * from students where name=:val",{'val': name})
  Student = namedtuple('Student', result.keys()) 
  students = [Student(*r) for r in result.fetchall()]
  students = [student.__dict__ for student in students]
  if len(students) != 0:
    return render_template('results.html', students=students)
  return redirect (url_for('land'))




@app.route('/profile/<id>', methods = ['GET', 'POST'])
def get_profile(id):
  #reviews = session.execute("select * from reviews where partnerid=:val", {'val': id})
  #Review = namedtuple('Review', result.keys())
  #reviews = [Review(*r) for r in reviews.fetchall()]
  #reviews = [review.__dict__ for review in reviews]
  #return render_template('student.html', reviews=reviews)
  return 'doop'

#select from taken, get only unique classes (i.e. ignore reviewers)

@app.route('/professors/<name>', methods = ['GET', 'POST'])
def get_profs(name):
  result = session.execute("select classID, prof from taken where prof=:val group by classID", {'val': name})
  profs = list(r for r in result.fetchall())
  if len(profs) != 0:
    return render_template('results.html', profs=profs)
  else:
    return redirect(url_for('land'))






@app.route('/create', methods=['GET', 'POST'])
def land():
  return render_template('create.html')
