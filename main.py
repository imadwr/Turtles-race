from turtle import Turtle, Screen
import random


def draw_track():
    track_turtle = Turtle(shape="turtle")
    track_turtle.pensize(3)
    track_turtle.color("CadetBlue2")
    position = -100
    for _ in range(7):
        track_turtle.penup()
        track_turtle.goto(x=-230, y=position)
        track_turtle.pendown()
        track_turtle.goto(x=230, y=position)
        position += 40
    track_turtle.hideturtle()


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="What turtle would win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-80, -40, 0, 40, 80, 120]
my_turtles = []


draw_track()

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    my_turtles.append(new_turtle)

if user_bet:
    race_on = True

while race_on:
    for turtle in my_turtles:
        distance = random.randint(0, 10)
        turtle.forward(distance)

        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won, the winner is {winning_color} turtle!")
            else:
                print(f"You've lost, the winner is {winning_color} turtle!")


screen.exitonclick()
