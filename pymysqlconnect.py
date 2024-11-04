import mysql.connector

db = mysql.connector.connect(host = 'localhost',user='root',password='root')

if db.is_connected():
    print("connected")
mycursr = db.cursor();
mycursr.execute("show databases")
for i in mycursr:
    print (i)
    
print()

'''mycursr.execute("create database newdb1")
mycursr.execute("show databases")
for i in mycursr:
    print (i)'''

mycursr.execute("use newdb")

'''mycursr.execute("create table newTeb (id int)")'''

mycursr.execute("show tables")

for i in mycursr:
    print(i)


