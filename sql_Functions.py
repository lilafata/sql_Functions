##########################################################################################################
#
# DATE  :      01/27/2025
# AUTHOR:      Lila Fata
# FILE  :      sql_Functions.py
# DESCRIPTION: This script file performs the following basic functions to manage a sqlite3 database:
#
#              * create Students database file
#              * insert records to Students Table
#              * update record in Students Table
#              * print all records in Students Table
#
# NOTE:
# 1) This program was executed using the IDLE Python 3.7 Shell on a Windows 10 laptop
# 2) Need to manually remove the db file prior to rerunning this script due to unique ID error
# 3) Will try looking into removing db file automatically in script
# 4) Sample Output 'sql_Functions_SAMPLEOutput.txt is included
#
##########################################################################################################

import os
import math
import re
import sqlite3


def main():
        
  connection = sqlite3.connect('students_database.db')
  db_cursor = connection.cursor()
  create_table_query = '''
  CREATE TABLE IF NOT EXISTS Students (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  age INTEGER,
  major TEXT);
  '''
  db_cursor.execute(create_table_query)
  print("\nsqlite3 student_database.db file with Students table successully created and connected!")
  
  db_cursor.execute('''
          INSERT INTO Students (id, name, age, major) VALUES
            (11, 'Jane Jones', 19, 'Economics'),
            (12, 'Michael Calhoun', 18, 'Electronics Engineering'),
            (13, 'Laura Hill', 17, 'Marketing'),
            (14, 'Tom Smith', 20, 'Information Technology');
        ''')
  print("\nStudents Table with records successfully inserted!")
  select_query = '''SELECT * FROM Students;'''
  data = db_cursor.execute(select_query)
  print("Students Table:")
  for student in data:
          print(student)

  sql_update_record_12_query = '''UPDATE Students SET major = 'Nursing' WHERE name = 'Laura Hill';'''
  db_cursor.execute(sql_update_record_12_query)
  print("\nStudents Table with one record successfully updated!")
  select_query = '''SELECT * FROM Students;'''
  data = db_cursor.execute(select_query)
  print("Students Table Updated:")
  for student in data:
          print(student)

  connection.commit()
  connection.close()
        

if __name__ == "__main__":
    main()
