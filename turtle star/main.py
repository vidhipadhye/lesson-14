import turtle 

turtle.Screen().bgcolor("Aqua")
board = turtle.Turtle()

#First triangle for the Star
board.forward(100) #Draw Base

board.left(120) 
board.forward(100)

board.left(120)
board.forward(100)

board.penup()
board.right(150)
board.forward(50)

#Second triangle for the star 

board.pendown()
board.right(90)
board.forward(100)  

board.right(120)
board.forward(100)

board.right(120)
board.forward(100)

turtle.done()