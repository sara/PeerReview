import csv
import names
import random
from random import randint
import MySQLdb
from app import engine

randint (00000, 99999)
#Generating all students - 5000 people in codebase in total



def main():
  con = engine.connect()
  #result = con.execute("select * from students")
  #for row in result:
  #  print("studentid:", row['studentid'])
  con = MySQLdb.connect("localhost", "root", "96Ladybug", "PeerReview")
  cursor = con.cursor()
  cursor.execute("SET sql_notes = 0; ")
  make_profs(con, cursor)
  #cursor.execute("create database IF NOT EXISTS PeerReview")
  #con.commit()

  #cursor.execute("create table IF NOT EXISTS students(studentid INTEGER, name VARCHAR (40), gender VARCHAR (6), gradyear INTEGER, gpa DOUBLE);")
  #con.commit()

  #cursor.execute("create table if not exists skills(reviewerid INTEGER, partnerid INTEGER, python INTEGER, c INTEGER, java INTEGER, javascript INTEGER, algo INTEGER, quality INTEGER, communication INTEGER, documentation INTEGER, accountability INTEGER, internships INTEGER);")
  #con.commit()

  #cursor.execute("create table if not exists taken(studentid INTEGER, class INTEGER);")

  #cursor.execute("create table if not exists reviews(class INTEGER, reviewerid INTEGER, partnerid INTEGER, grade INTEGER, percentage INTEGER, repartner INTEGER, prof VARCHAR (40));")
  #with open('students.csv', 'wb') as csvfile:
   # filewriter = csv.writer(csvfile, delimiter = ',', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
    #filewriter.writerow(['student_ID', 'name', 'gender', 'grad_year', 'GPA']) 
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

  #make_self_assessments(con, cursor)
  
  #cursor.execute("select * from skills")
  #cursor.execute("select * from skills")
  #fill_classes(con, cursor)
  #make_pairs(con, cursor, 213)
  #make_pairs(con, cursor, 214)
  #make_pairs(con, cursor, 336)
  #make_pairs(con, cursor, 344)
  #make_pairs(con, cursor, 352)
  #make_pairs(con, cursor, 416)
  #make_pairs(con, cursor, 440)
  
  #make_grades(con, cursor, 213, 0.24, 0.3, 0.32, 0.14)
  #make_grades(con, cursor, 214, 0.27, 0.32, 0.28, 0.13)
  #make_grades(con, cursor, 336, 0.2, 0.3, 0.34, 0.16)
  #make_grades(con, cursor, 344, 0.2, 0.25, 0.35, 0.2)
  #make_grades(con, cursor, 352, 0.22, 0.23, 0.36, 0.19)
  #make_grades(con, cursor, 416, 0.15, 0.25, 0.4, 0.2)
  #make_grades(con, cursor, 440, 0.18 ,0.27, 0.3, 0.25)
  
  #make_work_distribution(con, cursor, 213)
  #make_work_distribution(con, cursor, 214)
  #make_work_distribution(con, cursor, 336)
  #make_work_distribution(con, cursor, 344)
  #make_work_distribution(con, cursor, 352)
  #make_work_distribution(con, cursor, 416)
  #make_work_distribution(con, cursor, 440)
  
  #review_skills(con, cursor, 213)
  #review_skills(con, cursor, 214)
  #review_skills(con, cursor, 336)
  #review_skills(con, cursor, 344)
  #review_skills(con, cursor, 352)
  #review_skills(con, cursor, 416)
  #review_skills(con, cursor, 440)

  #review_repartner(con, cursor)

  #con.close()

def review_repartner(con, cursor):
  cursor.execute("select * from reviews")
  reviews = list(cursor.fetchall())
  for i in range(0, len(reviews)):
    curr = reviews.pop()
    percentage = curr[4]
    reviewer = curr[1]
    partner = curr[2]
    average = get_average_score(percentage, cursor, reviewer, partner)
    if average >= 0.5:
       cursor.execute("update reviews set repartner=1 where reviewerid=%s and partnerid=%s", (reviewer, partner))
    else:
      cursor.execute("update reviews set repartner=0 where reviewerid=%s and partnerid=%s", (reviewer, partner))
    con.commit()

def get_average_score(percentage, cursor, reviewer, partner):
  total = percentage
  num = 0
  cursor.execute("select * from skills where reviewerid=%s and partnerid=%s", (reviewer, partner))
  skillset = cursor.fetchone()
  for i in range (2, len (skillset)):
    if skillset[i] != None:
      print skillset[i]
      total += skillset[i]
      num += 3
  average = total/(float(num+100))
  print average 
  print(" ")
  return average

def review_skills(con, cursor, classcode):
   cursor.execute("select reviewerid, partnerid from reviews where class=%s" %(classcode))
   pair_list = list(cursor.fetchall())
   for i in range(0, len(pair_list)):
     pair = pair_list.pop()
     reviewer = pair[0]
     partner = pair[1]
     print (reviewer, partner)
     if classcode == 213:
       java = randint(1, 3)
       cursor.execute("update skills set java=%s where partnerid=%s and reviewerid=%s", (java, partner, reviewer))
     elif classcode == 214 or classcode == 416:
       c = randint(1, 3)
       cursor.execute("update skills set c=%s where partnerid=%s and reviewerid=%s", (c, partner, reviewer))
     elif classcode == 352:
       python = randint(1, 3)
       cursor.execute("update skills set python=%s where partnerid=%s and reviewerid=%s", (python, partner, reviewer))
     quality = randint(1, 3)
     communication = randint (1, 3)
     documentation = randint (1, 3)
     accountability = randint (1, 3)
     cursor.execute("update skills set quality=%s, communication=%s, documentation=%s, accountability=%s where partnerid=%s and reviewerid=%s", (quality, communication, documentation, accountability, partner, reviewer))
     con.commit()
    
def make_work_distribution(con, cursor, classcode):
  cursor.execute("select reviewerid, partnerid from reviews where class=%s" %(classcode))
  pair_list = list(cursor.fetchall())
  special_skill = False

  for i in range(0, len(pair_list)):
    pair = pair_list.pop()
    reviewer = pair[0]
    partner = pair[1]
    if classcode == 213:
      special_skill = True
      reviewer_skill = cursor.execute("select java from skills where reviewerid=%s and partnerid=%s" %(reviewer, reviewer))
      partner_skill = cursor.execute("select java from skills where reviewerid=%s and partnerid=%s" %(partner, partner))
    elif classcode == 214 or classcode == 416:
      special_skill = True
      reviewer_skill = cursor.execute("select c from skills where reviewerid=%s and partnerid=%s" %(reviewer, reviewer))
      partner_skill = cursor.execute("select c from skills where reviewerid=%s and partnerid=%s" %(partner, partner))
    elif classcode == 352:
      special_skill = True
      reviewer_skill = cursor.execute("select python from skills where reviewerid=%s and partnerid=%s" %(partner, partner))
      partner_skill = cursor.execute("select python from skills where reviewerid=%s and partnerid=%s" %(partner, partner))
    
    if special_skill:
      #diff =  reviewer_skill - partner_skill
      #partner's skills are equal or worse
      diff = 0
      if diff == 0:
        distr = randint(40, 60)
      elif diff == 1:
        distr = randint (30, 40)
      elif diff == 2:
        distr = randint (20, 40)

      #partner's skills are better
      elif diff == -1:
        distr = randint (50, 70)
      elif diff == -2:
        distr = randint (60, 80)
    
    else:
      distr = randint(0, 100)

    cursor.execute("update reviews set percentage=%s where reviewerid=%s and partnerid=%s", (distr, reviewer, partner))
    con.commit()

def make_grades(con, cursor, classcode, numA, numB, numC, numD):
  #softmeth
  cursor.execute("""select studentid from taken where class = %s order by rand()"""%(classcode))
  count = cursor.rowcount
  id_list = [item[0] for item in cursor.fetchall()]
  a = int(numA*count)
  b = int(numB*count)
  c = int(numC*count)
  d = int(numD*count)
  
  for i in range(0, a):
    print (i)
    reviewerid = id_list.pop()
    cursor.execute("update reviews set grade=%s where reviewerid=%s", ('4', reviewerid))
    con.commit()
  for i in range(0, b):
     print (i)
     reviewerid = id_list.pop()
     cursor.execute("update reviews set grade=%s where reviewerid=%s", ('3', reviewerid))
     con.commit()
  for i in range (0, c):
    print (i)
    reviewerid = id_list.pop()
    cursor.execute("update reviews set grade=%s where reviewerid=%s", ('2', reviewerid))
    con.commit()
  for i in range(0, d):
    print (i)
    reviewerid = id_list.pop()
    cursor.execute("update reviews set grade=%s where reviewerid=%s", ('1', reviewerid))
    con.commit()

def make_pairs(con, cursor, classcode):
  cursor.execute("""select studentid from taken where class = %s order by rand()""" %(classcode))
  id_list = list(cursor.fetchall())
  print(len(id_list))
  while (len(id_list)-1) > 0:
    reviewer = id_list.pop()
    partner = id_list.pop()
    cursor.execute("insert into reviews (class, reviewerid, partnerid ) values (%s, %s, %s)", (classcode, reviewer, partner))
    cursor.execute("insert into skills (reviewerid, partnerid) values (%s, %s)", (reviewer, partner))
    con.commit()

def make_self_assessments(con, cursor):
    #all freshman skills
    make_skill(con, cursor, 'python', 2021, 0.81, 0.09, 0.03)
    make_skill(con, cursor, 'java', 2021, 0.85, 0.13, 0.02)
    make_skill(con, cursor, 'c', 2021, 0.95, 0.045, 0.005)
    make_skill(con, cursor, 'javascript', 2021, 0.96, 0.02, 0.02)
    make_skill(con, cursor, 'documentation', 2021, 0.75, 0.15, 0.1)
    make_skill(con, cursor, 'algo', 2021, 0.2, 0.5, 0.3)
    make_skill(con, cursor, 'quality', 2021, 0.15, 0.45, 0.3)
    make_skill(con, cursor, 'communication', 2021, 0.04, 0.46, 0.50)
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

def fill_classes(con, cursor):
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
    #filewriter.writerow([make_ID(ID_list), name, gender, gradyear])
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
  print(intermediate)
  for i in range (0, intermediate):
    studentid = id_list.pop()
    cursor.execute("update skills set " + skill + "=%s where reviewerid=%s", ('2', studentid))
    con.commit()
  
  print('expert')
  print(expert)
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

def make_profs(con, cursor):
  cursor.execute("select reviewerid, partnerid from reviews where class=214")
  id_list = list(cursor.fetchall())
  for i in range(len(id_list)/2):
    curr = id_list.pop()
    reviewerid = curr[0]
    partnerid = curr[1]
    cursor.execute("update taken set prof=%s where class=214 and studentid=%s", ('Francisco', reviewerid)) 
    con.commit()
    cursor.execute("update taken set prof=%s where class=214 and studentid=%s", ('Francisco', partnerid)) 
    con.commit()
    cursor.execute("update reviews set prof=%s where reviewerid=%s and class=%s", ('Francisco', reviewerid, 214)) 
    con.commit()
 
  for i in range(len(id_list)/2):
    curr = id_list.pop()
    reviewerid = curr[0]
    partnerid = curr[1]
    cursor.execute("update taken set prof=%s where class=214 and studentid=%s", ('Santosh', reviewerid)) 
    con.commit()
    cursor.execute("update taken set prof=%s where class=214 and studentid=%s", ('Santosh', partnerid)) 
    con.commit()
    cursor.execute("update reviews set prof=%s where reviewerid=%s and class=%s", ('Santosh', reviewerid, 214)) 
    con.commit()
 
  



#SEE ABOVE - GIVE ALL CLASSES PROFESSORS, MAKE SURE PARTNER AND REVIEWER HAVE BOTH TAKEN SAME PROF AND THAT THE PROF IS IN THE REVIEW

  cursor.execute("select reviewerid, partnerid from reviews where class=336")
  id_list = list(cursor.fetchall())
  for i in range(len(id_list)/2):
    curr = id_list.pop()
    reviewerid = curr[0]
    partnerid = curr[1]
    cursor.execute("update taken set prof=%s where studentid=%s and class = 336", ('Imielinski', reviewerid))
    con.commit()
    cursor.execute("update taken set prof=%s where class=336 and studentid=%s", ('Imielinski', partnerid)) 
    con.commit()
    cursor.execute("update reviews set prof=%s where reviewerid=%s and class=%s", ('Imielinski', reviewerid, 336)) 
    con.commit()
  for i in range(len(id_list)):
    curr = id_list.pop()
    reviewerid = curr[0]
    partnerid = curr[1]
    cursor.execute("update taken set prof=%s where studentid=%s and class=336", ('Miranda', reviewerid)) 
    con.commit()
    cursor.execute("update taken set prof=%s where class=336 and studentid=%s", ('Miranda', partnerid)) 
    con.commit()
    cursor.execute("update reviews set prof=%s where reviewerid=%s and class=%s", ('Miranda', reviewerid, 336)) 
    con.commit()
 
  
  cursor.execute("select reviewerid, partnerid from reviews where class=344")
  id_list = list(cursor.fetchall())
  for i in range(len(id_list)/2):
    curr = id_list.pop()
    reviewerid = curr[0]
    partnerid = curr[1]
    cursor.execute("update taken set prof=%s where studentid=%s and class = 344", ('FarachColton', reviewerid)) 
    con.commit()
    cursor.execute("update taken set prof=%s where studentid=%s and class=344", ('FarachColton', partnerid)) 
    con.commit()
    cursor.execute("update reviews set prof=%s where reviewerid=%s and class=%s", ('FarachColton', reviewerid, 344)) 
    con.commit()
 
  for i in range(len(id_list)):
    curr = id_list.pop()
    reviewerid = curr[0]
    partnerid = curr[1]
    cursor.execute("update taken set prof=%s where studentid=%s and class= 344", ('Muthukrishnan', reviewerid)) 
    con.commit()
    cursor.execute("update taken set prof=%s where studentid=%s and class=344", ('Muthukrishnan', partnerid)) 
    con.commit()
    cursor.execute("update reviews set prof=%s where reviewerid=%s and class=%s", ('Muthukrishnan', reviewerid, 344)) 
    con.commit()
  
  
  cursor.execute("select reviewerid, partnerid from reviews where class=352")
  id_list = list(cursor.fetchall())
  for i in range(len(id_list)/2):
    curr = id_list.pop()
    reviewerid = curr[0]
    partnerid = curr[1]
    cursor.execute("update taken set prof=%s where class=352 and studentid=%s", ('Nath', reviewerid)) 
    con.commit()
    cursor.execute("update taken set prof=%s where class=352 and studentid=%s", ('Nath', partnerid)) 
    con.commit()
    cursor.execute("update reviews set prof=%s where reviewerid=%s and class=%s", ('Nath', reviewerid, 352)) 
    con.commit()
 
  for i in range(len(id_list)):
    curr = id_list.pop()
    reviewerid = curr[0]
    partnerid = curr[1]
    cursor.execute("update taken set prof=%s where class=352 and studentid=%s", ('Martin', reviewerid)) 
    con.commit()
    cursor.execute("update taken set prof=%s where class=352 and studentid=%s", ('Martin', partnerid)) 
    con.commit()
    cursor.execute("update reviews set prof=%s where reviewerid=%s and class=%s", ('Martin', reviewerid, 352)) 
    con.commit()
 
  
  cursor.execute("select reviewerid, partnerid from reviews where class=416")
  id_list = list(cursor.fetchall())
  for i in range(len(id_list)/2):
    curr = id_list.pop()
    reviewerid = curr[0]
    partnerid = curr[1]
    cursor.execute("update taken set prof=%s where class=416 and studentid=%s", ('PK', reviewerid)) 
    con.commit()
    cursor.execute("update taken set prof=%s where class=416 and studentid=%s", ('PK', partnerid)) 
    con.commit()
    cursor.execute("update reviews set prof=%s where reviewerid=%s and class=%s", ('PK', reviewerid, 416)) 
    con.commit()
 
  for i in range(len(id_list)):
    curr = id_list.pop()
    reviewerid = curr[0]
    partnerid = curr[1]
    cursor.execute("update taken set prof=%s where class=416 and studentid=%s", ('Francisco', reviewerid)) 
    con.commit()
    cursor.execute("update taken set prof=%s where class=416 and studentid=%s", ('Francisco', partnerid)) 
    con.commit()
    cursor.execute("update reviews set prof=%s where reviewerid=%s and class=%s", ('Francisco', reviewerid, 416)) 
    con.commit()
 
  
  cursor.execute("select reviewerid, partnerid from reviews where class=440")
  id_list = list(cursor.fetchall())
  for i in range(len(id_list)/2):
    curr = id_list.pop()
    reviewerid = curr[0]
    partnerid = curr[1]
    cursor.execute("update taken set prof=%s where class=440 and studentid=%s", ('Bekris', reviewerid)) 
    con.commit()
    cursor.execute("update taken set prof=%s where class=440 and studentid=%s", ('Bekris', partnerid)) 
    con.commit()
    cursor.execute("update reviews set prof=%s where reviewerid=%s and class=%s", ('Bekris', reviewerid, 440))
    con.commit()
 
  for i in range(len(id_list)):
    curr = id_list.pop()
    reviewerid = curr[0]
    partnerid = curr[1]
    cursor.execute("update taken set prof=%s where class=440 and studentid=%s", ('Bolaris', reviewerid)) 
    con.commit()
    cursor.execute("update taken set prof=%s where class=440 and studentid=%s", ('Bolaris', partnerid)) 
    con.commit()
    cursor.execute("update reviews set prof=%s where reviewerid=%s and class=%s", ('Bolaris', reviewerid, 440)) 
    con.commit()
 































def make_classes(con, cursor, classcode, f, s, j, se):
  print(classcode)
  cursor.execute("select studentid from students where gradyear=2021 order by rand()")
  #print (int(f*cursor.rowcount))
  id_list = [item[0] for item in cursor.fetchall()]
  for i in range(0, int(f*cursor.rowcount)):
    studentid = id_list.pop()
    #print x
    #print (cursor.fetchone())
    cursor.execute("insert into taken values (%s, %s)", (studentid, classcode))
    con.commit()
  cursor.execute("select studentid from students where gradyear=2020 order by rand()")
  id_list = [item[0] for item in cursor.fetchall()]
  for i in range(0, int(s*cursor.rowcount)):
    studentid = id_list.pop()
    #studentid = cursor.fetchone()
 #   print studentid
    cursor.execute("insert into taken values (%s, %s)", (studentid, classcode))
    con.commit()
  cursor.execute("select studentid from students where gradyear=2019 order by rand()")
  id_list = [item[0] for item in cursor.fetchall()]
  print(len(id_list))
  for i in range(0, int(j*cursor.rowcount)):
    if len(id_list) == 0:
      print i
    studentid = id_list.pop()
#    studentid = cursor.fetchone()
#    print studentid
    cursor.execute("insert into taken values (%s, %s)", (studentid, classcode))
    con.commit()
  cursor.execute("select studentid from students where gradyear=2018 order by rand()")
  id_list = [item[0] for item in cursor.fetchall()]
  for i in range(0, int(se*cursor.rowcount)):
    studentid = id_list.pop()
#    studentid = cursor.fetchone()
#    print studentid
    cursor.execute("insert into taken values (%s, %s)", (studentid, classcode))
    con.commit()


def make_ID(ID_list):
  range_start = 10**(4)
  range_end = (10**5)-1
  while True:
    num = randint(range_start, range_end)
    if num not in ID_list:
      ID_list.append(num)
      return num



if __name__ == "__main__":
  main()
