# print("=====Week 6 session 1=====")

# import os

# print("The current folder of my python code: ", os.getcwd())
# print("The POSIX interface for intercom:", os.name)

# print("List of all files in directory", os.listdir())
# print("List of all files in directory", os.listdir('/'))

# print("The current process ID", os.getpid())
# #print("creating a new folder:", os.mkdir("C:/Users/aws.admin/DOcuments/COM3003/Week7"))

# print("===============MATHS PLOT SECTION==============")

# # import matplotlib.pyplot as plt

# # #sample data
# # departments = ['HR', 'IT', 'Sales', 'Finance']
# # employees = [10, 25, 15, 12]

# # # create bar chart
# # plt.bar(departments, employees, color='skyblue')

# # # Add labels and title
# # plt.xlabel('Departments')
# # plt.ylabel('Number of Employees')
# # plt.title('Employee Distribution by Department')

# # #show chart
# # plt.show()

# # ages = [22, 25, 30, 30, 31, 34, 35, 36, 40, 41, 42, 45, 46, 50, 51, 52]

# # plt.hist(ages, bins=5, color='lightgreen', edgecolor='black')

# # plt.xlabel('Age Range')
# # plt.ylabel('Frequency')
# # plt.title('Age Distribution of Employees')

# # plt.show()

# # departments = ['HR', 'IT', 'Sales', 'Finance']
# # sizes = [10, 25, 15, 12]
# # colors = ['gold', 'skyblue', 'lightgreen', 'lightcoral']

# # plt.pie(sizes, labels=departments, colors=colors, autopct='%1.1f%%', startangle=90)

# # plt.axis('equal')
# # plt.title('Employee Percentage by Department')

# # plt.show()

# # x = [1, 2, 3, 4, 5]
# # y = [2, 4, 6, 8, 10]

# # plt.subplot(2, 2, 1)
# # plt.bar(x, y)
# # plt.title("Bar Chart")
# # plt.subplot(2, 2, 2)
# # plt.hist(y)
# # plt.title("Histogram")

# # plt.subplot(2, 2, 3)
# # plt.pie(y, labels=x)
# # plt.title("Pie Chart")

# # plt.subplot(2, 2, 4)
# # plt.plot(x, y, marker='o')
# # plt.title("Line Graph")

# # plt.tight_layout()
# # plt.show()

import turtle
screensize = turtle.getscreen()

Oogway = turtle.Turtle()




# screensize = turtle.getscreen()
# Oogway = turtle.Turtle()

# Oogway.right(90)
# Oogway.forward(130)
# Oogway.left(60)
# Oogway.back(100)
# Oogway.color("light green")

# Oogway.circle(60)
# Oogway.dot(60)

# Oogway.fd(100)
# Oogway.rt(90)
# Oogway.fd(100)
# Oogway.rt(90)
# Oogway.fd(100)
# Oogway.rt(90)
# Oogway.fd(100)

# my_wn = turtle.Screen()
# turtle.speed(2)

# for i in range(30):
#     turtle.circle(5*i)
#     turtle.color("red")
#     turtle.circle(-5*i)
#     turtle.color("blue")
#     turtle.left(i)
# #turtle.exitonclick()


# my_wn = turtle.Screen()
# turtle.speed(2)

# for i in range(30):
#     turtle.circle(5*i)
#     turtle.circle(-5*i)
#     turtle.left(i)
# #turtle.exitonclick()


colors = ['red', 'purple', 'blue', 'green', 'darkolivegreen', 'darksalmon']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100 + 1)
    t.forward(x)
    t.left(59)


turtle.mainloop()