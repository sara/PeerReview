from wtforms import Form, SelectMultipleField, RadioField, StringField, IntegerField, validators
from models import session, Students
from flask import render_template

class SearchForm(Form):
  studentid = StringField('Student Name')
  professorid = RadioField ('Professor Name', choices = [('Sesh', 'Sesh'), ('Imielinski', 'Imielinski'), ('Miranda', 'Miranda'), ('Muthukrishnan', 'Muthukrishnan'), ('Martin', 'Martin'), ('Francisco', 'Francisco'), ('Bolaris', 'Bolaris'), ('Santosh', 'Santosh'), ('FarachColton', 'FarachColton'), ('Nath', 'Nath'), ('PK', 'PK'), ('Bekris', 'Bekris')])
  
  classID =  RadioField('Class Code', choices = [('213', '213'),('214', '214'), ('336', '336'), ('344', '344'), ('352', '352'), ('416', '416'), ('440', '440')])
      
  def validate(form):
    student = form.data['studentid']
    prof = form.data['professorid']
    classID = form.data['classID']
    if prof != 'None' and student != 'None':
      return False
    if student != 'None' and classID != 'None':
      return False
    if prof != 'None' and classID != 'None':
      return False
    return True


class ProfileForm(Form):
  studentid = IntegerField('Student ID', [validators.InputRequired(message='Uh Oh! Looks like you forgot to put in an RUID')])
  name = StringField('Student Name', [validators.InputRequired( message='Uh Oh! Looks like you forgot to put in a name.')])
  gender = RadioField('Gender', choices = [('male', 'male'), ('female', 'female')])
  gradyear = RadioField('GradYear', [validators.InputRequired(message='Uh Oh! Looks like you forgot to put in a graduation year.')], choices = [('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021')])

  classID =  SelectMultipleField('Classes Taken - Select all that apply!', choices = [('213', '213'),('214', '214'), ('336', '336'), ('344', '344'), ('352', '352'), ('416', '416'), ('440', '440')])
  
  #def validate(form):
  #  studentid = form.data['studentid']
  #  name = form.data['name']
  #  gradyear = form.data['gradyear']
  #  return render_template('error.html', error = studentid, link="/")
  #  if not studentid:
  #    return render_template('error.html', error = 'Did you forget to put in an RUID?', link = "/create")
  #  else:
  #    return studentid
    #raise validators.ValidationError('Did you forget to put in an RUID?')
  #  if not name:
  #    return render_template('error.html', error = 'Did you forget to put in a name?', link = "/create")
    #raise validators.ValidationError('Did you forget to put in a name?')
  #  elif gradyear == 'None':
  #    return render_template('error.html', error = 'Did you forget to put in a grad year?', link = "/create")
    #raise validators.ValidationError('Did you forget to put in a grad year?')
  #duplicate = session.execute("select studentid from students where studentid=:val", {'val': studentid}).fetchall()
    #if duplicate:
    #  raise validators.ValidationError('Looks like that RUID is already registered!')
  #  return True
