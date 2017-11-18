from flask import request, render_template, redirect, url_for
from app import app, engine
from forms import SearchForm

@app.route('/', methods=['GET', 'POST'])
def landing():
  form = SearchForm(request.form)
  con = engine.connect()
  if request.method == 'POST' and form.validate():
    if form.data['studentid']:
      return get_student(form.data['studentid'], con)
  else:
    return render_template('land.html', form=form)

def get_student(name, con):
  result = con.execute("select * from students where name=%s", (name)).fetchall()
  result_dict = dict((col, getattr(studentid, name, gender, gradyear)) for col in result[0]
  if len(result_dict) != 0:
    return redirect(url_for('index', query=result))
  else:
    return redirect(url_for('land'))


@app.route('/results/<query>', methods=['GET', 'POST'])
def index(query):
  return render_template('results.html', results=query)

@app.route('/create', methods=['GET', 'POST'])
def land():
  return render_template('create.html')
    #  if any(i.isdigit() for i in s):
#    if (select * from students where studentid = student_identifier) != None:
#      return student_identifier
#    else:
#      return 'error'
#  elif any(i.isalpha() for i in student_identifier) = False:
#    if (select * from students where name=student_identifier) != None:
#      return student_identifier
#    else:
#      return student_identifier
#  else:
#    return "error, you put the string in wrong"


