from wtforms import Form, SelectMultipleField, RadioField, StringField, IntegerField, validators
from models import session, Students
from flask import render_template

class ReviewForm(Form):
  classID =  RadioField('Class Code', [validators.InputRequired(message='What class was this for?')], choices = [('213', '213'),('214', '214'), ('336', '336'), ('344', '344'), ('352', '352'), ('416', '416'), ('440', '440')])
  reviewerid = IntegerField('Reviewer ID', [validators.InputRequired(message='Looks like you didn\'t put in a reviewer ID')])
  partnerid = IntegerField('Partner ID', [validators.InputRequired(message='Looks like you didn\'t put in a partner ID')])
  grade = IntegerField('Grade', [validators.NumberRange(min=0, max=100, message='Not a valid grade'), validators.InputRequired(message='What did you get on the project?')])
  percentage = IntegerField('What percentage of work did they contribute?', [validators.NumberRange(min=0, max=100, message='Not a valid contribution range'), validators.InputRequired(message='Maybe your partner wasn\'t great, but you still need to list a work contribution!')])
  repartner = RadioField('Would you partner again?', [validators.InputRequired(message='Make sure you fill this out!')], choices = [('1', 'Yes'), ('0', 'No')])
  professorid = RadioField ('Professor Name', [validators.InputRequired(message='You forgot to select a professor')], choices = [('Sesh', 'Sesh'), ('Imielinski', 'Imielinski'), ('Miranda', 'Miranda'), ('Muthukrishnan', 'Muthukrishnan'), ('Martin', 'Martin'), ('Francisco', 'Francisco'), ('Bolaris', 'Bolaris'), ('Santosh', 'Santosh'), ('FarachColton', 'FarachColton'), ('Nath', 'Nath'), ('PK', 'PK'), ('Bekris', 'Bekris')])

class SearchForm(Form):
  studentid = StringField('Student Name')
  professorid = RadioField ('Professor Name', choices = [('Sesh', 'Sesh'), ('Imielinski', 'Imielinski'), ('Miranda', 'Miranda'), ('Muthukrishnan', 'Muthukrishnan'), ('Martin', 'Martin'), ('Francisco', 'Francisco'), ('Bolaris', 'Bolaris'), ('Santosh', 'Santosh'), ('FarachColton', 'FarachColton'), ('Nath', 'Nath'), ('PK', 'PK'), ('Bekris', 'Bekris')])
  
  classID =  RadioField('Class Code', choices = [('213', '213'),('214', '214'), ('336', '336'), ('344', '344'), ('352', '352'), ('416', '416'), ('440', '440')])
      
  def validate(form):
    student = form.data['studentid']
    prof = form.data['professorid']
    classID = form.data['classID']
    if prof != 'None' and student != '':
      return False
    if student != '' and classID != 'None':
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
