import turtle

window = turtle.Screen()
window.colormode(255)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 0, 0)]

def right():
    turtle.right(10)
    print("right pressed")
def left():
    turtle.left(10)
    print("left pressed")
def draw():
    turtle.fd(50)
def undo():
    turtle.undo()
def switch_color():
    set_color = (0, 0, 0)
    color = raw_input("Color: ")
    if color == "red":
        set_color = colors[0]
    elif color == "green":
        set_color = colors[1]
    elif color == "blue":
        set_color == colors[2]
    elif color == "black":
        set_color == colors[3]
    turtle.pencolor(set_color)
def pen_upDown():
    state = raw_input("up or down: ")
    if state == "up":
        turtle.penup()
    if state == "down":
        turtle.pendown()
def pen_up():
    turtle.penup()
def pen_down():
    turtle.pendown()
def clear_screen():
    turtle.clear()
     
turtle.onkey(right, "Right")
turtle.onkey(left, "Left")
turtle.onkey(draw, "space")
turtle.onkey(undo, "z")
turtle.onkey(switch_color, "c")
# turtle.onkey(pen_upDown, "a")
turtle.onkey(pen_up, "u")
turtle.onkey(pen_down, "d")
turtle.onkey(clear_screen, "v")

turtle.listen()
turtle.mainloop()
