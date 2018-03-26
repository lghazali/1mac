import turtle

def draw_init():
    #draw initials
    window = turtle.Screen()
    window.bgcolor("floralwhite")
    draw_L()
    draw_G()
    #draw_fin()
    window.exitonclick()

def draw_L():
   
    l = turtle.Turtle()
    l.shape("turtle")
    l.color("saddlebrown")
    l.pensize(10)
    l.speed(2)
    l.penup()
    l.setpos(0,0)
    l.pendown()
    l.right(90)
    l.forward(150)
    l.left(90)
    l.forward(90)
    l.penup()
    l.setpos(0,-190)


def draw_G():
    l = turtle.Turtle()
    l.shape("turtle")
    l.color("darkgreen")
    l.pensize(10)
    l.speed(2)
    l.penup()
    l.setpos(210,-45)
    l.pendown()
    l.left(90)
    l.forward(45)
    l.left(90)
    l.forward(90)
    l.left(90)
    l.forward(150)
    l.left(90)
    l.forward(90)
    l.left(90)
    l.forward(45)
    l.left(90)
    l.forward(22)
    l.penup()
    l.setpos(120,-190)

   
draw_init()

