from turtle import *

def walk():
    forward(200)
def walk_back():
    left(180)
    forward(200)
def go_and_back():
    walk()
    walk_back()

exitonclick ()