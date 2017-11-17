from flask import request, render_template
from app import app, engine
from forms import SearchForm

@app.route('/', methods=['GET', 'POST'])
def index():
  form = SearchForm(request.form)
  if request.method == 'POST' and form.validate():
    if form.data['studentid']:
      return get_student(form.data['studentid'])
    #if form.data['studentid']:
    #  return str(form.data['studentid'])
  
  else:
    #studentid = form.data['studentid']
    #if studentid != None:
      #return str(studentid)
  #con = engine.connect()
  #students = con.execute("select * from students")
  #ids = []
  #for row in students:
  #  ids.append(row[0])
    #x = row['studentid']
  #con.close()
  #return str(ids)
  #for row in result:
  #  print("studentid:", row['studentid'])
   return render_template('land.html', form=form)

def get_student(studentid):
  #identifier = request.form['student']
  #print identifier
  return 'doop'
  if any (i.isdigit() for i in identifier):
    return 'doop'
    if (con.execute("select * from students where studentid = %s", (identifier)) != Non):
      return 'hello world'
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


