# import pandas as pd
# import xlwt
# path = 'C:\\Users\\abhim\\Desktop\\example.txt'
# df=pd.read_csv(path,header=None)
# headers=['EMPID','Gender','AGE','SALES','BMI','INCOME']
# df.columns=headers
# df.to_excel('abc.xls')

# import pandas as pd
# from matplotlib import pyplot
# df=pd.read_csv('abc.csv')
# y=df.SALES
# x=df.Gender
# print(df)
# pyplot.xlabel('Gender')
# pyplot.ylabel('SALES')
# pyplot.title('Trial')
# pyplot.bar(x,y)
# pyplot.show()

# #Histogram :
# import matplotlib.pyplot as plt
# import pandas as pd
# fig=plt.figure() #Plots in matplotlib reside within a figure object, use plt.figure to create new figure
# #Create one or more subplots using add_subplot, because you can't create blank figure
# ax = fig.add_subplot(1,1,1)
# #Variable
# print(ax)
# df=pd.read_csv('abc.csv')
# ax.hist(df['AGE'],bins = 7) # Here you can play with number of bins
# print(df)
# # Labels and Tit
# plt.title('Age distribution')
# plt.xlabel('Age')
# plt.ylabel('#Employee')
# plt.show()

# import matplotlib.pyplot as plt
# import pandas as pd
# df=pd.read_csv('abc.csv')
# print(df)
# fig=plt.figure()
# ax = fig.add_subplot(1,1,1)
# #Variable
# ax.boxplot(df['AGE'])
# plt.show()

# import matplotlib.pyplot as plt
# import pandas as pd
# df = pd.read_csv('abc.csv')
# var=df.groupby('Gender').SALES.sum()
# fig=plt.figure()
# ax1=fig.add_subplot(1,1,1)
# ax1.set_xlabel('Gender')
# ax1.set_ylabel('Sum of Sales')
# ax1.set_title("Gender wise sum of sales")
# var.plot(kind='bar')
# plt.show()

# import matplotlib.pyplot as plt
# import pandas as pd
# df = pd.read_csv('abc.csv')
# var=df.groupby('BMI').SALES.sum()
# fig=plt.figure()
# ax1=fig.add_subplot(1,1,1)
# ax1.set_xlabel('BMI')
# ax1.set_ylabel('Sum of sales')
# ax1.set_title("BMI wise sum of sales")
# var.plot(kind='bar')
# plt.show()

# import matplotlib.pyplot as plt
# import pandas as pd
# df=pd.read_csv('abc.csv')
# fig=plt.figure()
# print(df)
# # ax1=fig.add_subplot(1,1,1)
# # ax1.scatter(df['AGE'],df['SALES'])
# # ax1.set_xlabel('Age')
# # ax1.set_ylabel('Sales')
# ax2=fig.add_subplot(1,1,1)
# ax2.scatter(df['AGE'],df['SALES'],s = df['INCOME'])
# ax2.set_xlabel('Age')
# ax2.set_ylabel('Sales')
# plt.show()

import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('abc.csv')
df['AGE1']=df.AGE
var=df.groupby(df['AGE1']).sum().stack()
print(var)
temp=var.unstack()
print('TEMP \n',temp)
x_list=temp['SALES']
plt.axis('equal')
plt.pie(x_list,labels=temp['AGE'],autopct="%1.1f%%")
plt.title("Pastafarianism Expenses")
plt.show()

# import matplotlib.pyplot as plt
# import pandas as pd
# df=pd.read_csv('abc.csv')
# print(df)
# # Pie chart, where the slices will be ordered and plotted counter-clockwise:
# labels = df.columns
# # var=df.groupby('').SALES.sum()
# sizes = [15, 30, 45, 10,30,40]
# explode = (0.2, 0, 0, 0,0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')

# fig1, ax1 = plt.subplots()
# ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
#         shadow=True, startangle=90)
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# plt.show()

# import matplotlib.pyplot as plt
# import pandas as pd
# df=pd.read_csv('abc.csv')
# print(df)
# # Pie chart, where the slices will be ordered and plotted counter-clockwise:
# labels = ['AGE', 'SALES']
# var=df.groupby(df['EMPID']).sum().stack()
# print(var)
# temp=var.unstack()
# sizes = var

# fig1, ax1 = plt.subplots()
# ax1.pie(temp['AGE'], labels=temp, autopct='%1.1f%%',
#         shadow=True, startangle=90)
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# plt.show()

# import matplotlib.pyplot as plt
# import pandas as pd
# df=pd.read_csv('abc.csv')
# # print(df.describe())
# # print(df["Gender"].value_counts())
# print(df.groupby(['Gender']).mean())
# plt.pie(df['INCOME'],labels = df.Gender, autopct="%1.1f%%")
# plt.xlabel('AGE')
# plt.ylabel('SALES')
# # plt.show()