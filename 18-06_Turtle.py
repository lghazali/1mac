import turtle

def draw_square ():
    window = turtle.Screen()
    window.bgcolor("floralwhite")

    leonardo = turtle.Turtle()
    leonardo.shape("turtle")
    leonardo.color("saddlebrown")
    leonardo.speed(2)
    d = 150
    a = 90

    i = 0
    while i < 4:
         leonardo.right(a)
         leonardo.forward(d)
         i += 1
    window.exitonclick()
    
draw_square()