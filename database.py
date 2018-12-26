# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="",
#   database="mydatabase"
# )

# mycursor = mydb.cursor()

# # mycursor.execute("CREATE DATABASE mydatabase")


# mycursor = mydb.cursor()

# # mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")


# # sql = "INSERT INTO emp (name,id) VALUES (%s,%d)"
# # val=("Sunny", 22)
# id =222
# string='hola'

# mycursor.execute("INSERT INTO emp VALUES(%s,%s)", (string,int(id)))
# mydb.commit()
# # myresult = mycursor.fetchall()

# # for x in myresult:
# #   print(x)

import pandas as pd

data = pd.read_csv("proj.csv")
data.head()