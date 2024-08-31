import mysql.connector #imports package
#creates connection object
mydb= mysql.connector.connect(host='localhost',user='root',passwd='password',database='school')

#creates cursor instance
cursor= mydb.cursor()

#creates new table
s='''Create table students 
   (ID integer,
    Marks integer,
    Name char(25));'''
cursor.execute(s)
mydb.commit()

#inserting values into table
cursor.execute('''insert into students
               values(1,34,'Rahul');''')
mydb.commit()
cursor.execute('''insert into students
               values(2,63,'Rohit');''')
mydb.commit()
cursor.execute('''insert into students
               values(3,70,'subham');''')
mydb.commit()               

#checking number of students passed
#executes the query and stores the results as tuples in cursor object
cursor.execute('select * from students where marks>40;')


data= cursor.fetchall()
count=cursor.rowcount()#counts number of rows in data
print('Total number of students passed:',count)

for row in data:#prints all received records
    print(row)
    
cursor.close()
mydb.close()


