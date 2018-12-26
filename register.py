import pathlib
import mysql.connector
def register():
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="mydatabase"
        )
        mycursor = mydb.cursor()
        email=input("Enter your email ")
        path=pathlib.Path("{}.txt".format(email))
        if path.exists() == True:
                print("Already Registered , please login ")
        else:     
                name=input("Enter your name ")
                password=input("Enter your password ")
                fi=open("{}.txt".format(email),"w")
                fi.write(name)
                fi.write(",")
                fi.write(password)
                id =222
                string='hola'
                mycursor.execute("INSERT INTO users VALUES(%s,%s,%s)", (email,name,password))
                mydb.commit()
                print("Successfully Registered ")
    # fi=open("foo.txt","a")
    # fi.write("Hello\n")
    # os.remove("foo.txt")"{}.txt".format(email))
