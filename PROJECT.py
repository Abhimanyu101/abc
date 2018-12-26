import register
import login
import mysql.connector
n=0
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="",
#   database="mydatabase")
# mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE users1 (email VARCHAR(255), name VARCHAR(255), password VARCHAR(255))")
# mydb.commit()
while n!=3:
    print("Press 1 to login ")
    print("Press 2 to Register")
    print("Press 3 to Exit")
    n=int(input("Enter your choice "))
    if n==1:
        login.login()
    elif n==2:
        register.register()