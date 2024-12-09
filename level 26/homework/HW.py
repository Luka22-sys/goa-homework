import turtle

def draw_triangle(side_length):
    for _ in range(3):
        turtle.forward(side_length)
        turtle.left(120)

odd_numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


turtle.speed(10) 
turtle.penup()
turtle.goto(-200, 200) 

counter = 0
for i in range(len(odd_numbers)):
    for j in range(i, len(odd_numbers)):
        for k in range(j, len(odd_numbers)):
            if counter >= 120:
                break
            side_length = odd_numbers[counter % len(odd_numbers)]
            draw_triangle(side_length)
            turtle.penup()
            turtle.forward(50) 
            counter += 1
        if counter >= 120:
            break
    if counter >= 120:
        break

turtle.done()