import csv
import names
import random
from random import randint
import MySQLdb

randint (00000, 99999)
#Generating all students - 5000 people in codebase in total



def main():
#  db = MySQLdb.connect("localhost", "root", "96Ladybug", "PeerReview")
 # cursor = db.cursor()
 # cursor.execute("SET sql_notes = 0; ")
 # cursor.execute("create database IF NOT EXISTS PeerReview")

#  cursor.execute("create table IF NOT EXISTS students(studentid INTEGER, name VARCHAR (40), gender VARCHAR (6), gradyear INTEGER, gpa DOUBLE);")

  with open('students.csv', 'wb') as csvfile:
    filewriter = csv.writer(csvfile, delimiter = ',', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
    filewriter.writerow(['student_ID', 'name', 'gender', 'grad_year', 'GPA']) 
    ID_list = []
    make_students(filewriter, cursor, 114, ID_list, 'female', 2021)
    make_students(filewriter, cursor, 386, ID_list, 'male', 2021)
    make_students(filewriter, cursor, 213, ID_list, 'female', 2020)
    make_students(filewriter, cursor, 1037, ID_list, 'male', 2020)
    make_students(filewriter, cursor, 235, ID_list, 'female', 2019)
    make_students(filewriter, cursor, 1265, ID_list, 'male', 2019)
    make_students(filewriter, cursor, 263, ID_list, 'female', 2018)
    make_students(filewriter, cursor, 1487, ID_list, 'male', 2018)
    db.commit()
    db.close()

def make_students(filewriter, cursor, num_students, ID_list, gender, gradyear):
  for i in range(0, num_students):
    GPA = '{0:.2f}'.format(random.uniform(0.0, 4.0))
    name = names.get_full_name(gender=gender)
    studentid = make_ID(ID_list)
    print (name)
    cursor.execute("insert into students (studentid, name, gender, gradyear, gpa) values (%s, %s, %s, %s, %s)", (studentid, name, gender, gradyear, GPA))
    filewriter.writerow([make_ID(ID_list), name, gradyear, GPA])


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