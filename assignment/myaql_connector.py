#import sqlite3
import mysql.connector
#creating database/connect
join = mysql.connector.connect(user='root', password='',host='localhost')
#creating cursor
c=join.cursor()
#to execute sql query
c.execute("""CREATE DATABASE zoos;""")
c.execute("""USE zoos""")
