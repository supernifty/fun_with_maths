#!/usr/bin/env python

# estimates pi by calculating the ares of a polygon contained and containing a circle
# as suggested by Archimedes

# e.g. python estimate_pi result.eps

import math
import sys
import turtle

RADIUS=20
SPACE=80
XMAX=200

def estimate(sides, canvas):
    # inner area
    angle = 2 * math.pi / sides / 2
    area = math.cos(angle) * math.sin(angle)
    lower_bound = sides * area

    # outer area
    area = math.tan(angle) * 1
    upper_bound = sides * area
    sys.stdout.write('{} sides: {:.3f} to {:.3f}\n'.format(sides, lower_bound, upper_bound))

    pos = turtle.position()
    # add image
    
    # outer poly
    turtle.setpos(pos[0], pos[1] - RADIUS / math.cos(angle) + RADIUS)
    turtle.pen(fillcolor="green")
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(RADIUS / math.cos(angle), steps=sides)
    turtle.end_fill()
    turtle.penup()

    # circle
    turtle.setpos(pos[0], pos[1])
    turtle.pen(fillcolor="red")
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(RADIUS)
    turtle.end_fill()
    turtle.penup()
    
    # inner poly
    turtle.setpos(pos[0], pos[1])
    turtle.pen(fillcolor="yellow")
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(RADIUS, steps=sides)
    turtle.end_fill()
    turtle.penup()

    turtle.setpos(pos[0] + 2 * RADIUS, pos[1])
    turtle.write('{} sides\nLow: {:.3f}\nHigh: {:.3f}\n'.format(sides, lower_bound, upper_bound))

def estimate_pi(side_list, target):
    ymax = SPACE + len(side_list) * SPACE
    turtle.getscreen().setup(XMAX, ymax, 0, 0)
    ts = turtle.getscreen().getcanvas()
    ts = turtle.getscreen().reset()
    turtle.speed(0)
    turtle.penup()
    ymax = turtle.window_height()
    y = ymax / 2 - SPACE 
    for iteration in side_list:
        turtle.setpos(-RADIUS, y)
        estimate(iteration, ts)
        y -= SPACE

    turtle.hideturtle()
    turtle.getcanvas().postscript(file = target)

if __name__ == '__main__':
    estimate_pi([3,4,5,6,7,8,9,10,100,1000], sys.argv[1])
