from wtforms import Form, RadioField, StringField, IntegerField, validators
from models import session, Students


class SearchForm(Form):
  studentid = StringField('Student Name')
  professorid = StringField('Professor Name')
  classID =  IntegerField('Class Code')

  def validate(form):
    student = form.data['studentid']
    prof = form.data['professorid']
    classcode = form.data['classID']
    if student and prof:
      raise validators.ValidationError('Must search for only one field at a time')
    if student and classcode:
      raise validators.ValidationError('Must search for only one field at a time')
    if prof and classcode:
      raise validators.ValidationError('Must search for only one field at a time')
    return True


class ProfileForm(Form):
  studentid = IntegerField('Student ID')
  name = StringField('Student Name')
  gender = RadioField('Gender', choices = [('male', 'male'), ('female', 'female')])
  gradyear = RadioField('GradYear', choices = [('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021')])

  def validate(form):
    studentid = form.data['studentid']
    name = form.data['name']
    gradyear = form.data['gradyear']
    
    if studentid is None:
      raise validators.ValidationError('Did you forget to put in an RUID?')
    elif not name: 
      raise validators.ValidationError('Did you forget to put in a name?')
    elif gradyear == 'None':
      raise validators.ValidationError('Did you forget to put in a grad year?')
    duplicate = session.execute("select studentid from students where studentid=:val", {'val': studentid}).fetchall()
    if duplicate:
      raise validators.ValidationError('Looks like that RUID is already regsitered!')
    return True
