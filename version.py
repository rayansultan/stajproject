import mysql.connector

db= mysql.connector.connect(host="localhost",
                            port=3306,
                            user="root",
                            password="",
                            database="exam"
                             )
mycursor=db.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS exam")

mycursor.execute(" ALTER TABLE questions ADD FOREIGN KEY (id) REFERENCES quiz (id) ")
db.commit()
#mycursor.execute("CREATE TABLE quiz ( id INT(8) NOT NULL  ,name VARCHAR (100) NOT NULL,description VARCHAR(600) NOT NULL,success_mark INT(8) NOT NULL , created_at YEAR NOT NULL ) ")
#mycursor.execute("CREATE TABLE questions (id INT (8) NOT NULL,title varchar(255) NOT NULL ,quiz_id bigint NOT NULL)")
#mycursor.execute("UPDATE TABLE choices (id INT(8),title varchar(255) NOT NULL,question_id bigint ,is_correct boolean NOT NULL)")
#mycursor.execute("CREATE TABLE students (id INT NOT NULL UNIQUE,first_name varchar(255) NOT NULL,last_name varchar(255) NOT NULL)")
#mycursor.execute("CREATE TABLE student_results (id INT NOT NULL,student_id bigint NOT NULL,quiz_id bigint NOT NULL,question_iD bigint NOT NULL,choice_id bigint NOT NULL,is_correct boolean NOT NULL,score tinyint NOT NULL)")
#mycursor.execute(" ALTER TABLE questions ADD FOREIGN KEY (id) REFERENCES quiz (id) ")