from wtforms import Form, RadioField, StringField, IntegerField, validators
from models import session, Students


class SearchForm(Form):
  studentid = StringField('Student Name')
  professorid = RadioField ('Professor Name', choices = [('Sesh', 'Sesh'), ('Imielinski', 'Imielinski'), ('Miranda', 'Miranda'), ('Muthukrishnan', 'Muthukrishnan'), ('Martin', 'Martin'), ('Francisco', 'Francisco'), ('Bolaris', 'Bolaris'), ('Santosh', 'Santosh'), ('FarachColton', 'FarachColton'), ('Nath', 'Nath'), ('PK', 'PK'), ('Bekris', 'Bekris')])
  
  
  #professorid =  RadioField('Professor Name', choices = [('213', '213'),('214', '214'), ('336', '336'), ('344', '344'), ('352', '352'), ('416', '416'), ('440', '440')])
  
  classID =  RadioField('Class Code', choices = [('213', '213'),('214', '214'), ('336', '336'), ('344', '344'), ('352', '352'), ('416', '416'), ('440', '440')])
      
  def validate(form):
    student = form.data['studentid']
    prof = form.data['professorid']
    classID = form.data['classID']
    if student and prof:
      raise validators.ValidationError('Must search for only one field at a time')
    if student and classID:
      raise validators.ValidationError('Must search for only one field at a time')
    if prof != 'None' and classID != 'None':
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
