import turtle

def turtle_forward():
    turtle.forward(50)
    turtle.stamp()

def turtle_right():
    turtle.right(90)
    turtle.forward(50)
    turtle.stamp()

def turtle_left():
    turtle.left(90)
    turtle.forward(50)
    turtle.stamp()

def turtle_back():
    turtle.right(180)
    turtle.forward(50)
    turtle.stamp()

def restart():
    turtle.reset()

turtle.shape('turtle')

turtle.onkey(turtle_forward, 'w')
turtle.onkey(turtle_right, 'd')
turtle.onkey(turtle_left, 'a')
turtle.onkey(turtle_back,  's')
turtle.onkey(restart, 'Escape')
turtle.listen()
