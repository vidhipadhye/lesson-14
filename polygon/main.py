import turtle 
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle()   #Defined variable 

num_sides = 6     #variables
side_length = 70
angle = 360 / num_sides
#iterate loop for total number of sides 
for i in range(num_sides):
    polygon.forward(side_length) 
    polygon.left(angle)        

turtle.done()