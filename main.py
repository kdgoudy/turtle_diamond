from turtle import Turtle, Screen

s = Turtle()
screen = Screen()
screen.setup(700, 500)

s.penup()
s.setpos(-200,200)
s.pendown()
s.forward(400)
s.setheading(295)
s.forward(80)
s.setheading(220)
s.forward(300)
s.setheading(140)
s.forward(310)
s.setheading(63)
s.forward(75)
s.end_fill()

screen.exitonclick()
