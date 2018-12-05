#import sqlite3
import mysql.connector
#creating database/connect
join = mysql.connector.connect(user='root', password='dushyant',host='localhost')
#creating cursor
c=join.cursor()
#to execute sql query
#c.execute("""CREATE DATABASE zoos;""")
c.execute("""USE zoos""")
c.execute("""CREATE TABLE zoo(animal TEXT,id INTEGER,water_need INTEGER)""")
#open csv file
#read csv file
import csv
with open('zoo.csv') as zoo_data:
    csv_reader = csv.reader(zoo_data, delimiter =',')
    next(csv_reader)
    for row in csv_reader:
        c.execute("""INSERT INTO zoo(animal,id,water_need) VALUES('{}',{},{})""".format(str(row[0]),row[1],row[2]))
c.execute("""SELECT * FROM zoo""")
fetch = c.fetchall()
for i in fetch:
    print i[0]," ",i[1]," ",i[2]
