from wtforms import Form, StringField, IntegerField, validators

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
