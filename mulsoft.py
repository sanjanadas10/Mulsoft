import sqlite3 as sql

connection = sql.connect("dabaseMovies.db")

pointer = connection.cursor()
pointer.execute("CREATE TABLE IF NOT EXISTS MOVIES( MOVIE_NAME TEXT, ACTOR TEXT, ACTRESS TEXT,DIRECTOR_NAME TEXT, YEAR INTEGER )")
pointer.execute("INSERT INTO MOVIES VALUES('Bhool Bhulaiyaa 2','Kartik Aaryan','Kiara Advani','Anees Bazmee',2022)")
pointer.execute("INSERT INTO MOVIES VALUES('Jugjugg Jeeyo','Varun Dhawan','Kiara Advani','Raj Mehta',2022)")
pointer.execute("INSERT INTO MOVIES VALUES('Jersey','Shahid Kapoor','Mrunal Thakur','Gowtam Tinnanuri',2022)")
pointer.execute("INSERT INTO MOVIES VALUES('Baaghi 3','Tiger Shroff','Shraddha Kapoor','Ahmed Khan',2020)")
pointer.execute("INSERT INTO MOVIES VALUES('Shershaah','Sidharth Malhotra','Kiara Advani','Vishnuvardhan',2021)")

# Printing all the elements of the database 
allMovies = pointer.execute("SELECT * FROM MOVIES").fetchall()
for i in allMovies:
  title,actor,actress,director,releasedYear = i
  print("{t}\t\t{a}\t\t{ats}\t\t{d}\t\t{ry}".format(t=title,a=actor, ats=actress,d=director,ry=releasedYear))

# In this query, we are printing only the details from the db where Kiara Advani is the lead actress
actorQuery = pointer.execute("SELECT * FROM MOVIES WHERE ACTRESS = 'Kiara Advani'").fetchall()
for i in actorQuery:
  title,actor,actress,director,releasedYear = i
  print("{t}\t\t{a}\t\t{ats}\t\t{d}\t\t{ry}".format(t=title,a=actor, ats=actress,d=director,ry=releasedYear))
  