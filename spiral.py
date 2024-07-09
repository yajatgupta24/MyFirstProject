import turtle
import colorsys  # librarires
t = turtle.Turtle() # new turtle object
s = turtle.Screen().bgcolor('black') # creates a screen
t.speed(0)
n = 70 # number color sets
h = 0
for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h+= 1/n
    t.color(c)
    t.left(1)
    t.fd(1)
    for j in range(2):
        t.left(2)
        t.circle(100)

#=============

from turtle import *
import colorsys

speed(0)
bgcolor("black")
h = 0
for i in range(16):
    for j in range(18):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        color(c)
        h += 0.005
        rt(90)
        circle(150 - j * 6, 90)
        lt(90)
        circle(150 - j * 6, 90)
        rt(180)
    circle(40, 24)
done()

#=====

from turtle import*
import colorsys
speed(90)
hideturtle()
bgcolor("black")
tracer(5)
width(2)
h=0.01
for i in range(55):
	color(colorsys.hsv_to_rgb(h,1,1))
	forward(100)
	left(60)
	forward(100)
	right(120)
	circle(50)
	left(240)
	forward(100)
	left(60)
	forward(100)
	h+=0.02
	color(colorsys.hsv_to_rgb(h,1,1))
	forward(100)
	left(60)
	forward(100)
	right(120)
	circle(-50)
	left(240)
	forward(100)
	left(60)
	forward(100)
	left(2)
	h+=0.02
done()