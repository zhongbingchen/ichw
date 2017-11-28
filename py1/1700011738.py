#!/usr/bin/env python3

"""Foobar.py: Description of what foobar does.

__author__ = "Zhong Bingchen"
__pkuid__  = "1700011738"
__email__  = "1700011738@pku.edu.cn"
"""

import math
import turtle

def planet(name, color, center, long, short):
    name = turtle.Turtle()
    name.speed(0)
    name.shape("circle")
    name.color(color)
    name.penup()
    name.goto(center+long,0)
    name.pendown()
    for i in range(629):
        name.goto(center+long*math.cos(i/100),short*math.sin(i/100))


def main():
    sun = turtle.Turtle()
    sun.shape("circle")
    sun.color("red")
    sun.shapesize(2, 2, 1)
    planet(1, "yellow", 0, 40, 50)
    planet(2, "green", 25, 60, 40)
    planet(3, "blue", 50, 100, 50)
    planet(4, "black", 60, 130, 100)
    planet(5, "sea green", 60, 180, 110)
    planet(6, "purple", 50, 250, 150)
    

if __name__ == '__main__':
    main()
