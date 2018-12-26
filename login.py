import pathlib
import profile
import mysql.connector
def login():
        email=input("Enter your email ")
        path=pathlib.Path("{}.txt".format(email))
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="mydatabase"
        )
        mycursor = mydb.cursor()
        password=input("Enter your password ")
        mycursor.execute("SELECT * FROM users WHERE email = '" + email + "' AND password = '" + password + "'")
        result=mycursor.fetchall()
        
        if len(result) == 0:
            print("Invalid Email or Password , please try again ")
        else:
            for x in result:
                print("Successfuly Logged in")
                print(x)
                profile.update(email)
                        