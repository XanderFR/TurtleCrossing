import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
carManager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.goUp, "Up")

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Make and move the cars across the screen
    carManager.createCar()
    carManager.moveCars()

    # Detect turtle collision with a car
    for car in carManager.allCars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.gameOver()

    # Detect turtle making it across the street
    if player.isAtFinishLine():
        player.gotToStart()
        carManager.levelUp()  # Make the cars speed up on the next level
        scoreboard.increaseLevel()

screen.exitonclick()
