from turtle import *
window=Screen()
window.bgcolor("black")

turtle1 = Turtle()
turtle1.color("red")
turtle1.shape("turtle")
turtle1.width(9)

turtle2 =Turtle()
turtle2.color("blue")
turtle2.shape("turtle")
turtle2.width(9)


for player in range(6):
    turtle1.penup()
    turtle1.goto(-400,190)
    turtle1.pendown()
    
    for steps in range(15):
        turtle1.penup()
        turtle1.fd(50)
        turtle1.pendown()
        turtle1.write("sojjy")

for player2 in range(6):
    turtle2.penup()
    turtle2.goto(-400,90)
    turtle2.pendown()

    for steps in range(15):
        turtle2.penup()
        turtle2.fd(50)
        turtle2.pendown()
        turtle2.write("Codes")


window.exitonclick()