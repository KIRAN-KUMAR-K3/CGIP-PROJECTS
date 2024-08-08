import turtle
import math

screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(1)  
t.pensize(2)

def draw_rectangle(x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

def draw_circle(x, y, radius, color):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.color(color)
    t.circle(radius)

def translate(dx, dy):
    t.penup()
    t.goto(t.xcor() + dx, t.ycor() + dy)
    t.pendown()

def rotate(x, y, angle):
    current_x, current_y = t.pos()
    angle_rad = math.radians(angle)
    new_x = x + math.cos(angle_rad) * (current_x - x) - math.sin(angle_rad) * (current_y - y)
    new_y = y + math.sin(angle_rad) * (current_x - x) + math.cos(angle_rad) * (current_y - y)
    t.penup()
    t.goto(new_x, new_y)
    t.setheading(t.heading() + angle)
    t.pendown()

def scale(x, y, sx, sy):
    current_x, current_y = t.pos()
    new_x = x + (current_x - x) * sx
    new_y = y + (current_y - y) * sy
    t.penup()
    t.goto(new_x, new_y)
    t.shapesize(stretch_wid=sx, stretch_len=sy)
    t.pendown()

draw_rectangle(-200, 0, 100, 50, "blue")

translate(200, 0)
draw_rectangle(0, 0, 100, 50, "blue")

rotate(0, 0, 45)
draw_rectangle(0, 0, 100, 50, "blue")

scale(0, 0, 2, 2)
draw_rectangle(0, 0, 100, 50, "blue")

draw_circle(100, 100, 50, "red")

translate(200, 0)
draw_circle(300, 100, 50, "red")

rotate(300, 100, 45)
draw_circle(300, 100, 50, "red")

scale(300, 100, 2, 2)
draw_circle(600, 200, 50, "red")

turtle.done()
