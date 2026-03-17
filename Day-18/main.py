######## Challenge 1 - Draw a Square ############
import turtle as t

tim = t.Turtle()

for _ in range(4):
    tim.forward(100)
    tim.left(90)



########### Challenge 2 - Draw a Dashed Line ########
for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()