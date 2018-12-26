# # example of a line plot
# from numpy import sin
# from matplotlib import pyplot
# # consistent interval for x-axis
# x = [x*0.1 for x in range(100)]
# # function of x for y-axis
# y = sin(x)
# # create line plot
# pyplot.plot(x, y)
# # show line plot
# pyplot.show()

# # example of a bar chart
# from random import seed
# from random import randint
# from matplotlib import pyplot
# # seed the random number generator
# seed(1)
# # names for categories
# x = ['red', 'green', 'blue']
# print(randint(0,100))
# # quantities for each category
# y = [randint(0, 100), randint(0, 100), randint(0, 100)]
# # create bar chart
# pyplot.bar(x, y)
# # show line plot
# pyplot.show()



# # example of a histogram plot
# from numpy.random import seed
# from numpy.random import randn
# from matplotlib import pyplot
# # seed the random number generator
# seed(1)
# # random numbers drawn from a Gaussian distribution
# x = randn(1000)
# print(x)
# # create histogram plot
# pyplot.hist(x)
# # show line plot
# pyplot.show()



# # example of a box and whisker plot
# from numpy.random import seed
# from numpy.random import randn
# from matplotlib import pyplot
# # seed the random number generator
# seed(1)
# # random numbers drawn from a Gaussian distribution
# x = [randn(1000), 5 * randn(1000), 10 * randn(1000)]
# # create box and whisker plot
# print(x)
# pyplot.boxplot(x)
# # show line plot
# pyplot.show()

# # example of a scatter plot
# from numpy.random import seed
# from numpy.random import randn
# from matplotlib import pyplot
# # seed the random number generator
# seed(1)
# # first variable
# x = 20 * randn(1000) + 100
# # second variable
# y = x + (10 * randn(1000) + 50)
# # create scatter plot
# pyplot.scatter(x, y)
# # show line plot
# pyplot.show()

from numpy.random import seed
from numpy.random import randn
from numpy import cos
from matplotlib import pyplot
seed(1)
x=15+10*randn(1000)
y=x+20*cos(x)+20
pyplot.scatter(x,y)
pyplot.show()
