from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.allCars = []
        self.carSpeed = STARTING_MOVE_DISTANCE

    def createCar(self):
        randomChance = random.randint(1, 6)
        if randomChance == 1:  # If block to prevent too many cars from cluttering the screen
            newCar = Turtle("square")
            newCar.shapesize(stretch_wid=1, stretch_len=2)  # Rectangular shape
            newCar.penup()
            newCar.color(random.choice(COLORS))
            randomY = random.randint(-250, 250)  # Ensures cars appear along the middle of the screen
            newCar.goto(300, randomY)
            self.allCars.append(newCar)

    def moveCars(self):
        for car in self.allCars:
            car.backward(self.carSpeed)  # Car movement from right to left

    def levelUp(self):
        self.carSpeed += MOVE_INCREMENT
