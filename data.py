import csv
import names
import random
from random import randint
import MySQLdb

randint (00000, 99999)
#Generating all students - 5000 people in codebase in total



def main():
  con = MySQLdb.connect("localhost", "root", "96Ladybug", "PeerReview")
  cursor = con.cursor()
  cursor.execute("SET sql_notes = 0; ")
  cursor.execute("create database IF NOT EXISTS PeerReview")
  con.commit()

#  cursor.execute("create table IF NOT EXISTS students(studentid INTEGER, name VARCHAR (40), gender VARCHAR (6), gradyear INTEGER, gpa DOUBLE);")
 # con.commit()

  #cursor.execute("create table if not exists skills(reviewerid INTEGER, partnerid INTEGER, python INTEGER, c INTEGER, java INTEGER, javascript INTEGER, algo INTEGER, quality INTEGER, communication INTEGER, documentation INTEGER, accountability INTEGER, internships INTEGER);")
 # con.commit()

  #cursor.execute("create table if not exists taken(studentid INTEGER, class INTEGER);")
#  fill_classes(con, cursor)

#  cursor.execute("create table if not exists reviews(
  #with open('students.csv', 'wb') as csvfile:
  #  filewriter = csv.writer(csvfile, delimiter = ',', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
   # filewriter.writerow(['student_ID', 'name', 'gender', 'grad_year', 'GPA']) 
    #ID_list = []

 
    #make_students(filewriter, cursor, 114, ID_list, 'female', 2021)
    #make_students(filewriter, cursor, 386, ID_list, 'male', 2021)
    #make_students(filewriter, cursor, 213, ID_list, 'female', 2020)
    #make_students(filewriter, cursor, 1037, ID_list, 'male', 2020)
    #make_students(filewriter, cursor, 235, ID_list, 'female', 2019)
    #make_students(filewriter, cursor, 1265, ID_list, 'male', 2019)
    #make_students(filewriter, cursor, 263, ID_list, 'female', 2018)
    #make_students(filewriter, cursor, 1487, ID_list, 'male', 2018)
    #con.commit()

  make_self_assessments(con, cursor)
  cursor.execute("select * from skills")
  
  
  con.close()


def make_self_assessments(con, cursor):
    #all freshman skills
    make_skill(con, cursor, 'python', 2021, 0.81, 0.09, 0.03)
    make_skill(con, cursor, 'java', 2021, 0.85, 0.13, 0.02)
    make_skill(con, cursor, 'c', 2021, 0.95, 0.045, 0.005)
    make_skill(con, cursor, 'javascript', 2021, 0.96, 0.02, 0.02)
    make_skill(con, cursor, 'documentation', 2021, 0.75, 0.15, 0.1)
    make_skill(con, cursor, 'algo', 2021, 0.2, 0.5, 0.3)
    make_skill(con, cursor, 'quality', 2021, 0.15, 0.45, 0.3)
    make_skill(con, cursor, 'communication', 2020, 0.14, 0.46, 0.50)
    make_skill(con, cursor, 'accountability', 2021, 0.03, 0.3, 0.67)
    make_skill(con, cursor, 'internships', 2021, 0.97, 0.03, 0.0, 0.0)

    #all sophomore skills
    make_skill(con, cursor, 'python', 2020, 0.77, 0.18, 0.05)
    make_skill(con, cursor, 'java', 2020, 0.75, 0.18, 0.05)
    make_skill(con, cursor, 'c', 2020, 0.95, 0.045, 0.005)
    make_skill(con, cursor, 'javascript', 2020, 0.90, 0.07, 0.03)
    make_skill(con, cursor, 'documentation', 2020, 0.4, 0.4, 0.2)
    make_skill(con, cursor, 'algo', 2020, 0.5, 0.05, 0.15)
    make_skill(con, cursor, 'quality', 2020, 0.07, 0.68, 0.25)
    make_skill(con, cursor, 'communication', 2020, 0.12, 0.33, 0.55)
    make_skill(con, cursor, 'accountability', 2020, 0.06, 0.25, 0.69)
    make_skill(con, cursor, 'internships', 2020, 0.92, 0.05, 0.03, 0.0)

    #all junior skills
    make_skill(con, cursor, 'python', 2019, 0.65, 0.25, 0.1)
    make_skill(con, cursor, 'java', 2019, 0.70, 0.2, 0.07)
    make_skill(con, cursor, 'c', 2019, 0.65, 0.3, 0.05)
    make_skill(con, cursor, 'javascript', 2019, 0.85, 0.1, 0.05)
    make_skill(con, cursor, 'documentation', 2019, 0.2, 0.45, 0.2)
    make_skill(con, cursor, 'algo', 2019, 0.2, 0.6, 0.2)
    make_skill(con, cursor, 'quality', 2019, 0.05, 0.45, 0.4)
    make_skill(con, cursor, 'communication', 2019, 0.1, 0.3, 0.6)
    make_skill(con, cursor, 'accountability', 2019, 0.04, 0.28, 0.68)
    make_skill(con, cursor, 'internships', 2019, 0.8, 0.1, 0.1)

    #all senior skills
    make_skill(con, cursor, 'python', 2018, 0.5, 0.27, 0.13)
    make_skill(con, cursor, 'java', 2018, 0.6, 0.3, 0.1)
    make_skill(con, cursor, 'c', 2018, 0.55, 0.38, 0.07)
    make_skill(con, cursor, 'javascript', 2018, 0.79, 0.15, 0.06)
    make_skill(con, cursor, 'documentation', 2018, 0.1, 0.5, 0.40)
    make_skill(con, cursor, 'algo', 2018, 0.1, 0.6, 0.3)
    make_skill(con, cursor, 'quality', 2018, 0.01, 0.29, 0.7)
    make_skill(con, cursor, 'communication', 2018, 0.1, 0.3, 0.6)
    make_skill(con, cursor, 'accountability', 2018, 0.05, 0.23, 0.72)
    make_skill(con, cursor, 'internships', 2018, 0.39, 0.3, 0.2, 0.08, 0.03)

#def fill_classes(con, cursor):
    make_classes(con, cursor, 213, 0.03, 0.05, 0.3, 0.4)
    make_classes(con, cursor, 214, 0.02, 0.3, 0.6, 0.9)
    make_classes(con, cursor, 336, 0.01, 0.1, 0.4, 0.85)
    make_classes(con, cursor, 344, 0.0, 0.1, 0.5, 1)
    make_classes(con, cursor, 352, 0.0, 0.01, 0.2, 0.4)
    make_classes(con, cursor, 416, 0.0, 0.03, 0.15, 0.25)
    make_classes(con, cursor, 440, 0.0, 0.03, 0.15, 0.25)


#GPA is a result of student grades in courses, NOT something that is inherent of a student herself
def make_students(filewriter, cursor, num_students, ID_list, gender, gradyear):
  for i in range(0, num_students):
    name = names.get_full_name(gender=gender)
    studentid = make_ID(ID_list)
    print (name)
    cursor.execute("insert into students (studentid, name, gender, gradyear) values (%s, %s, %s, %s)", (studentid, name, gender, gradyear))
    filewriter.writerow([make_ID(ID_list), name, gender, gradyear])
    cursor.execute("insert into skills(reviewerid, partnerid, python, c, java, javascript, algo, quality, communication, documentation, accountability, internships) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (studentid, studentid, '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'))


def make_skill(con, cursor, skill, gradyear, l1, l2, l3, l4=0, l5=0):
  cursor.execute("""select studentid from students where gradyear = %s order by rand()""" %(gradyear))
  beginner = int(cursor.rowcount*l1)
  intermediate = int(cursor.rowcount*l2)
  expert = int(cursor.rowcount*l3)
  super_expert = int(cursor.rowcount*l4)
  print ("THE STATS: ", skill, gradyear, cursor.rowcount, l1, l2, l3, l4, beginner, intermediate, expert, super_expert)
  id_list = [item[0] for item in cursor.fetchall()]
  
  print('beginner')
  print(len(id_list))
  for i in range (0, beginner):
    studentid = id_list.pop()
    cursor.execute("update skills set " + skill + "=%s where reviewerid = %s", ('1', studentid))
    con.commit()
  
  print('intermediate')
  print(len(id_list))
  for i in range (0, intermediate):
    studentid = id_list.pop()
    cursor.execute("update skills set " + skill + "=%s where reviewerid=%s", ('2', studentid))
    con.commit()
  
  print('expert')
  print(len(id_list))
  for i in range (0, expert):
    if len(id_list) == 0:
      print i
    studentid = id_list.pop()
    cursor.execute("update skills set " + skill + "=%s where reviewerid=%s", ('3', studentid))
    con.commit()
 
  print('super_expert')
  print(len(id_list))
  for i in range(0, super_expert):
    studentid = id_list.pop()
    cursor.execute("update skills set " + skill + "=%s where reviewerid=%s", ('4', studentid))
    con.commit()



def make_classes(con, cursor, classcode, f, s, j, se):
  cursor.execute("select studentid from students where gradyear=2021")
  print (int(f*cursor.rowcount))
  for i in range(0, int(f*cursor.rowcount)):
    x = cursor.fetchone()
    print x
    #print (cursor.fetchone())
    cursor.execute("insert into taken values (%s, %s)", (classcode, x))
    #con.commit()
  #cursor.execute("select studentid from students where gradyear=2020 order by rand()")
 # for i in range(0, int(s*cursor.rowcount)):
 #   studentid = cursor.fetchone()
 #   print studentid
 #   cursor.execute("insert into taken values (%s, %s)", (classcode, studentid))
 #   con.commit()
 # cursor.execute("select studentid from students where gradyear=2019 order by rand()")
#  for i in range(0, int(j*cursor.rowcount)):
#    studentid = cursor.fetchone()
#    print studentid
#    cursor.execute("insert into taken values (%s, %s)", (classcode, studentid))
#    con.commit()
#  cursor.execute("select studentid from students where gradyear=2018 order by rand()")
#  for i in range(0, int(se*cursor.rowcount)):
#    studentid = cursor.fetchone()
#    print studentid
#    cursor.execute("insert into taken values (%s, %s)", (classcode, studentid))
#    con.commit()


def make_ID(ID_list):
  range_start = 10**(4)
  range_end = (10**5)-1
  while True:
    num = randint(range_start, range_end)
    if num not in ID_list:
      num = randint(range_start, range_end)
      ID_list.append(num)
      return num



if __name__ == "__main__":
  main()
