# Turtle Party Project
# By Danielle Arnett
# 9/21/22

import turtle
turtle.color("blue")

# print("Hello World")

# size = 200

# turtle.right(120)
# turtle.forward(50)
# turtle.right(120)
# turtle.forward(50)
# turtle.right(120)
# turtle.forward(50)

size = 120

# Triangle pointed down
def upward_triangle(size):
  for i in range(3):
    turtle.forward(size)
    turtle.left(120)
  
# Triangle pointed up
def downward_triangle(size):
  for i in range(3):
    turtle.right(120)
    turtle.forward(size)

# Helper functions 
def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()
  
def forward(len):
  back(-1 * len)
  


# Triangle tests
# upward_triangle(100)
# back(75)
# upward_triangle(50)
# back(50)
# upward_triangle(25)
# forward(25)
# downward_triangle(25)
# forward(75)
# downward_triangle(50)
# forward(125)
# downward_triangle(100)

# Square
def square(size):
  for i in range(2):
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    
# Testing Square
# square(100)
# back(75)
# square(50)
# back(50)
# square(25)

# Polygon
def polygon(num_sides, len_side):
  for i in range(num_sides):
    turtle.forward(len_side)
    turtle.left(360/num_sides)
    
# Testing Polygon
# polygon(6,75)
# back(100)
# polygon(5,50)
# back(50)
# polygon(4,25)

    
# for n in range(3, 10):
#   forward(50)
#   polygon(n, 100/n)
#   back(50)
#   turtle.right(360/7)


# Spiral
def spiral(len_long, angle):
  for i in range(len_long, 1, -3):
    turtle.forward(i)
    turtle.left(angle)

spiral(75, 45)

   



    
