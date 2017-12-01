from flask import request, render_template, redirect, url_for
from app import app
from forms import SearchForm, ProfileForm, ReviewForm
from sqlalchemy import inspect, exc
from models import session, Reviews, Taken, Students 
from collections import namedtuple
from urllib import quote


@app.route('/', methods=['GET', 'POST'])
def landing():
  search_form = SearchForm(request.form)
  if request.method == 'POST':
    if search_form.validate():
      if search_form.data['studentid']:
        return redirect(url_for('get_students', name=search_form.data['studentid']))
      elif search_form.data['professorid'] != 'None':
        return redirect(url_for('get_profs', name=search_form.data['professorid']))
      elif search_form.data['classID']:
        return redirect(url_for('get_class', classID=search_form.data['classID']))
    else:
      return render_template('error.html', error = 'Uh Oh! Make sure to only search one field at a time.', link = "/", destination = 'home')
  else:
    return render_template('land.html', form=search_form)



@app.route('/classes/<classID>', methods = ['GET', 'POST'])
def get_class(classID):
  reviews = session.execute("select * from reviews where classID=:val",{'val': classID})
  review = namedtuple('review', reviews.keys())
  reviews = [review(*r) for r in reviews.fetchall()]
  reviews = [review.__dict__ for review in reviews]
  for review in reviews:
    reviewer=get_name(review['reviewerid'])
    partner=get_name(review['partnerid'])
    review['reviewerid']=reviewer
    review['partnerid']=partner
  average = get_average_grade(classID)
  diversity = round(get_diversity(classID), 4)*100
  #best = get_extreme_partners(classID, True)
  #worst = get_extreme_partners(classID, False)
  
  return render_template('class.html', diversity = diversity, classID = classID, average = average, reviews=reviews)


@app.route('/program', methods = ['GET'])
def program():
  stats = get_all_stats(False)
  levels = get_all_stats(True)
  return render_template('program.html', levels=levels, stats=stats) 


def get_all_stats(aggregate):
  soft_meth = round(get_diversity(213), 4)*100
  systems = round(get_diversity(214), 4) *100
  databases = round(get_diversity(336), 4)*100
  algo = round(get_diversity(344), 4) *100
  os = round(get_diversity(416), 4)*100
  it = round(get_diversity(352), 4)*100
  ai = round(get_diversity(440), 4)*100
  if aggregate:
    return [('200 level: ', (soft_meth+systems)/2), ('300 level: ', round((databases+algo+it)/3), 4), ('400 level: ', (os+ai)/2)]
  else: 
    return [('Software Methodology', soft_meth, get_average_grade(213)), ('Systems Programming',  systems, get_average_grade(214)), ('Databases', databases, get_average_grade(336)), ('Algorithms', algo, get_average_grade(344)),  ('Internet Technology', it, get_average_grade(352)), ('Operating Systems', os, get_average_grade(416)), ('Artificial Intelligence', ai, get_average_grade(440))]




def get_diversity(classID):
  women = session.execute("select count(studentid) from taken where classID=:val and studentid in (select studentid from students where gender=:gender)", {'val':classID, 'gender': 'female'})
  women = int(women.fetchone()[0])*1.0
  men = session.execute("select count(studentid) from taken where classID=:val and studentid in (select studentid from students where gender=:gender)", {'val':classID, 'gender': 'male'})
  men = int(men.fetchone()[0])*1.0
  return (women/(women+men))




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


@app.route('/best_and_worst', methods=['GET'])
def get_extreme_partners():
  reviews = session.execute("select * from reviews where percentage>=50 and repartner=1 and grade>=3")
  review = namedtuple('review', reviews.keys())
  reviews = [review(*r) for r in reviews.fetchall()]
  best = [review.__dict__ for review in reviews]
  for review in best:
    reviewer = get_name(review['reviewerid'])
    partner = get_name(review['partnerid'])
    review['reviewerid']=reviewer
    review['partnerid']=partner


  reviews = session.execute("select * from reviews where percentage<50 and repartner=0 and grade<3")
  review = namedtuple('review', reviews.keys())
  reviews = [review(*r) for r in reviews.fetchall()]
  worst = [review.__dict__ for review in reviews]
  for review in worst:
    reviewer = get_name(review['reviewerid'])
    partner = get_name(review['partnerid'])
    review['reviewerid']=reviewer
    review['partnerid']=partner
  return render_template('wall.html', best=best, worst=worst)

def get_name(studentid):
  name = session.execute("select name from students where studentid=:val", {'val':studentid}).fetchone()[0]
  return name

def get_average_grade(classID):
  average = session.execute("select avg (grade) from reviews where classID=:val", {'val': classID}).fetchone()[0]
  average = round(average, 2)
  if average <2:
    return ['F', average]
  if average < 3:
    return ['C', average]
  if average < 4:
    return ['B', average]
  return ['A', average]


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
      return render_template('error.html', error='Uh oh - it looks like that RUID is already registered.', link = "/create", destination  = 'back')
    return render_template('student.html', name=name, ruid=studentid, reviews=[], confirmation = 'Partner has been added to database!')
  return render_template('create_profile.html', form = form)

@app.route('/review', methods = ['GET', 'POST'])
def review():
  review_form = ReviewForm(request.form)
  profile_form = ProfileForm()
  if request.method == 'POST' and review_form.validate():
    reviewerid = review_form['reviewerid']
    partnerid = review_form['partnerid']
    reviewerid = int(reviewerid.raw_data[0])
    partnerid = int(partnerid.raw_data[0])
    classID = review_form['classID']
    classID = int(classID.raw_data[0])
    percentage = review_form['percentage']
    percentage = int(percentage.raw_data[0])
    repartner = review_form['repartner']
    repartner = int(repartner.raw_data[0])
    prof = review_form['professorid']
    prof = str(prof.raw_data[0])
    grade = review_form['grade']
    grade = int(grade.raw_data[0])/25
    
    #make sure that the reviewer has a profile - if they don't make them make one
    if len(student_exists(reviewerid)) == 0:
      return render_template('create_profile.html', form=profile_form,  error='No fair reviewing a friend if you don\'t have your own profile! Make one before you proceed.')
    if len(student_exists(partnerid)) == 0:
      return render_template('create_profile.html', form=profile_form,  error='That person\'s not registered yet. Make a profile for them before you review!')
    
    #make sure that both are listed as having taken the class
    if taken_class(reviewerid, classID) == 0:
      session.execute("insert into taken(classID, studentID) values (:classID, :reviewerid)", {'reviewerid': reviewerid, 'classID':classID})
    if taken_class(partnerid, classID) == 0:
      session.execute("insert into taken(classID, studentID) values (:classID, :partnerid)", {'partnerid': partnerid, 'classID':classID})
    try:
      session.execute("insert into reviews (classID, reviewerid, partnerid, grade, percentage, repartner, prof) values (:classID, :reviewerid, :partnerid, :grade, :percentage, :repartner, :prof)", {'classID': classID, 'reviewerid': reviewerid, 'partnerid': partnerid, 'grade': grade, 'percentage': percentage, 'repartner': repartner, 'prof': prof})
      session.commit()
      return redirect(url_for('get_student_profile', id=partnerid))
    except exc.SQLAlchemyError:
      return render_template('error.html', error='Hey now - you can\'t take a class more than once. You or your partner is already registered.', link = "/review", destination  = 'back')
  return render_template('create_review.html', form=review_form)

def student_exists(studentid):
  result = session.execute("select name from students where studentid=:val",{'val': studentid}).fetchall()
  students = list(r for r in result)
  student = list(r for r in result)
  return students


def taken_class(studentid, classID):
  result = session.execute("select studentid from taken where studentid=:val and classID = :classID", {'val':studentid, 'classID':classID}).fetchall()
  student = list(r for r in result)
  return len(student)
