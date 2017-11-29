from flask import request, render_template, redirect, url_for
from app import app
from forms import SearchForm, ProfileForm
from sqlalchemy import inspect, exc
from models import session, Reviews, Taken, Students 
from collections import namedtuple
from urllib import quote


@app.route('/', methods=['GET', 'POST'])
def landing():
  form = SearchForm(request.form)
  if request.method == 'POST':
    if form.validate():
      if form.data['studentid']:
        return redirect(url_for('get_students', name=form.data['studentid']))
      elif form.data['professorid'] != 'None':
        return redirect(url_for('get_profs', name=form.data['professorid']))
      elif form.data['classID']:
        return redirect(url_for('get_class', classID=form.data['classID']))
    else:
      return render_template('error.html', error = 'Uh Oh! Make sure to only search one field at a time.', link = "/")
  else:
    return render_template('land.html', form=form)



@app.route('/classes/<classID>', methods = ['GET', 'POST'])
def get_class(classID):
  reviews = session.execute("select * from reviews where classID=:val",{'val': classID})
  review = namedtuple('review', reviews.keys())
  reviews = [review(*r) for r in reviews.fetchall()]
  reviews = [review.__dict__ for review in reviews]
  average = get_average_grade(classID)
  return render_template('class.html', classID = classID, average = average, reviews=reviews)

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




@app.route('/student_profile/<id>', methods = ['GET', 'POST'])
def get_student_profile(id):
  reviews = session.execute("select * from reviews where partnerid=:val", {'val': id})
  review = namedtuple('review', reviews.keys())
  reviews = [review(*r) for r in reviews.fetchall()]
  reviews = [review.__dict__ for review in reviews]
  name = session.execute("select name from students where studentid = :val", {'val': id})
  name = name.fetchone()[0]
  for review in reviews:
    r_name = session.execute("select name from students where studentid=:val", {'val': review['reviewerid']})
    review['reviewerid'] = r_name.fetchone()[0]
    p_name = session.execute("select name from students where studentid=:val", {'val': review['partnerid']})
    review['partnerid'] = p_name.fetchone()[0]
  return render_template('student.html', name=name, ruid=id, reviews=reviews)


def get_average_grade(classID):
  average = session.execute("select avg (grade) from reviews where classID=:val", {'val': classID}).fetchone()[0]
  if average <2:
    return ['F', average]
  if average < 3:
    return ['C', average]
  if average < 4:
    return ['B', average]
  return ['A', average]

def get_average_rating(reviews):
  #gradesum = session.execute("select sum(grade) as gradesum from reviews where partnerid=:val", {'val':studentid}).fetchone()[0]
  #contribution = session.execute("select sum(percentage) as contribution from reviews where partnerid=:val", {'val':studentid}).fetchone()[0]
  #gradesum = session.execute("select review.
  
  #return gradesum
  num = 0
  total = len(reviews)*200
  for review in reviews:
    num = num + 25* int(review['grade'])
    num = num + int(review['percentage'])
  #average = num/total
  return len(reviews)#num/total
  #return 'doop'



@app.route('/professor_profile/<id>/<course>', methods = ['GET', 'POST'])
def get_professor_profile(id, course):
  reviews = session.execute("select * from reviews where prof=:val and classID=:course", {'val': id, 'course': course })
  review = namedtuple('review', reviews.keys())
  reviews = [review(*r) for r in reviews.fetchall()]
  reviews = [review.__dict__ for review in reviews]
  for review in reviews:
    r_name = session.execute("select name from students where studentid=:val", {'val': review['reviewerid']})
    review['reviewerid'] = r_name.fetchone()[0]
    p_name = session.execute("select name from students where studentid=:val", {'val': review['partnerid']})
    review['partnerid'] = p_name.fetchone()[0]
  #average_grade = get_average_grade(reviews) 
  return render_template('prof.html', reviews=reviews, prof=id, course=course)


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
  form = ProfileForm(request.form)
  if request.method == 'POST' and form.validate():
    studentid = form.data['studentid']
    name = form.data['name']
    gender = form.data['gender']
    gradyear = form.data['gradyear'] 
    try:
      session.execute("insert into students (studentid, name, gender, gradyear) values (:studentid, :name, :gender, :gradyear)", {'studentid': studentid, 'name':name, 'gender': gender, 'gradyear': gradyear})
      session.commit()
    except exc.SQLAlchemyError:
      return render_template('error.html', error='Uh oh - it looks like that RUID is already registered.', link = "/create")
    return 'Partner has been added to the database!'
  return render_template('create_profile.html', form = form)


