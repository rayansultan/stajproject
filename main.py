import mysql.connector
from questionmodel import Question
from QUESTIONS import question_data
from quizmodel import QuizModel
db= mysql.connector.connect(host="localhost",
                            port=3306,
                            user="root",
                            password="",
                            database="exam"
                             )
mycursor=db.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS exam")

# lname=input("Enter your last name:")
# sid=input(" Enter your student's number:")
# fname=input("Enter your first name: ")
# sql="INSERT INTO student (id,first_name,last_name) VALUES (%s,%s,%s)"
# added_values=(sid,fname,lname)
# mycursor.execute(sql,added_values)
mycursor.execute("SHOW TABLES")
for i in mycursor:
    print(i)
#db.commit()