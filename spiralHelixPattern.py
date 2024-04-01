import turtle 
import random

loadWindow = turtle.Screen() 
turtle.speed(0) 

for i in range(100): 
    turtle.color(random.random(), random.random(), random.random())  # Random RGB color
    turtle.circle(5*i) 
    turtle.circle(-5*i) 
    turtle.left(i) 

turtle.exitonclick() 
